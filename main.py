import uvicorn
from etl.extract import download
from etl.load import load


def main():
    data = download()
    load(data)
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
    
    
if __name__ == '__main__':
    main()