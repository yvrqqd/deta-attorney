from fastapi import FastAPI
import pymorphy2

morph = pymorphy2.MorphAnalyzer(lang='ru')

app = FastAPI()

@app.get("/")
def root():
    return "Hello from Space! 🚀"

@app.get("/parser")
def to_parse(name: str, job: str):
    Job_im = job.lower().capitalize()
    job_rod = " ".join([morph.parse(i.lower())[0].inflect({'gent'}).word for i in job.split(" ")])
    name_rod = " ".join([morph.parse(i)[0].inflect({'gent'}).word for i in name.split(" ")]).title()
    tmp = name.split(" ")
    surname = tmp[0]
    name_im = "".join([i[0]+'.' for i in tmp[1:]])+" "+surname
    
    return {"Job_im":Job_im, "job_rod":job_rod, "name_rod":name_rod, "name_im":name_im}
