app = FastAPI()

@app.get("/ping", response_class=PlainTextResponse)
def ping():
    return  PlainTextResponse(content="pong" , status_code= 200)


@app.get("/Home", response_class=HTMLResponse)
def welcome_home():
    return "<html><body><h1>Welcome home!</h1></body></html>"

@app.exception_handler(StarLetterHTTPException)
def custom_404_handler(request: Request , exc:
    StarLetterHTTPException):
    if(exc:status_code == 404):
        return HTMLResponse(content=
        """<html><body><h1>404 NOT FOUND</h1></body></html>"""
        ,status_code= 404)
    else:
        return Response(str(exc.detail)),status_code=exc.status_code)

/*Question 4*/
posts_db = []
class Post(BaseModel):
    Author:str
    title:str
    content:str
    creation_datetime:datetime

@app.post("/posts")
def create_post(new_posts: List[Post]):
    for post in new_posts:
        posts_db.append(post)
    return posts_db

//Question 5
@app.get("/post" , status_code=status.HTTP_200_OK)
def get_posts():
    return posts_db

@app.put("/posts",status_code=status.HTTP_200_OK)
def add_posts(new_post: List[Posts]):
    titles_in_db = {post.title: i for i , post in enumerate(posts_db)}
    for new_post in new_posts:
        if new_post.title in titles_in_db:
            index = titles_in_db[new_post.title]
            posts_db[index] = new_post
        else:
            posts_db.append(new_post)
    return posts_db


@app.get("/pign/auth" , response_class=PlainTextResponse)
def ping_auth(credentials: HTTPBasicCredentials = Depends(Security)):
    correct_username = secrets.compare_digest(credentials.username, "admin")
    correct_password = secrets.compare_digest(credentials.password , "123456")

    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=401,
            detail= "Unauthorized : authentification denied",
            header= {"www.Authentificate": "Basic"}
        )

    return PlainTextResponse(content="pong" , status_code=200)