
from fastapi import APIRouter,HTTPException
from fastapi.openapi.utils import status_code_ranges

from pymodel.post import UserPost, UserPostIn, Comment, CommentIn, UserPostWithComments

router = APIRouter()

post_table = {}
comment_table = {}

def find_post(post_id):
    return post_table.get(post_id)

@router.post("/post",response_model=UserPost,status_code=201)
async def create_post(post:UserPostIn):
    data = post.model_dump()
    last_record_ids= len(post_table)
    new_post = {**data,"id":last_record_ids}
    post_table[last_record_ids]=new_post
    return new_post

@router.get("/post",response_model=list[UserPost])
async def get_all_post():
    return list(post_table.values())


@router.post("/comment",response_model=Comment)
async def create_comment(comment:CommentIn):
    post = find_post(comment.post_id)
    if not post:
        raise HTTPException(status_code=404,detail="Post not found")

    data = comment.model_dump()
    last_record_ids= len(comment_table)
    new_comment = {**data,"id":last_record_ids}
    comment_table[last_record_ids]=new_comment
    return new_comment

@router.get("/post/{post_id}/comment",response_model=list[Comment])
async def get_comment_on_post(post_id:int):
    return [comment for comment in comment_table.values() if comment["post_id"] == post_id]

#@router.get("/post/{post_id",response_model=UserPostWithComments)
@router.get("/post/{post_id",response_model=UserPostWithComments)
async def get_comment_on_post(post_id:int):
    post = find_post(post_id)
    if not post:
        raise HTTPException(status_code=404,detail="Post not found")

    return {
        "post":post,
        "comment": await get_comment_on_post(post_id)
    }
