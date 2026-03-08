from get_subtitle import get_subtitles
from transformers import BartTokenizer, BartForConditionalGeneration
import sqlite3

def init_database():
    conn = sqlite3.connect("summary.db")
    cur = conn.cursor()
    res=cur.execute("SELECT name FROM sqlite_master")
    db_exists=res.fetchone()[-1]
    if db_exists=="summary":
        return cur
    else:
        cur.execute("CREATE TABLE summary(url text,length integer,value text)")
        return cur

def get_summary(url):
    cur = init_database()
    
    subtitles = get_subtitles(url)
    tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn')
    model = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')
    input_tensor = tokenizer.encode( subtitles, return_tensors="pt", max_length=512)
    outputs_tensor = model.generate(input_tensor, max_length=160, min_length=120, length_penalty=2.0, num_beams=4, early_stopping=True)


    print(tokenizer.decode(outputs_tensor[0]))

get_summary("https://www.youtube.com/watch?v=lv1_-RER4_I")
init_database()