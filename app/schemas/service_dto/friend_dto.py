from pydantic import BaseModel
from typing import Literal, Optional, List

class FriendApplyInput(BaseModel):
    sender_id: str
    receiver_id: str
    sender_friend_list: Optional[list]
    
class FriendApplyOutput(BaseModel):
    status: Literal["success", "already_friend", "already_send"]
    
class FriendApplyResInput(BaseModel):
    consent_status: bool
    sender_id: str
    receiver_id: str

class FriendApplyResOutput(FriendApplyResInput):
    pass

class FriendSearchInput(BaseModel):
    search_word: str
    
class FriendSearchData(BaseModel):
    id: Optional[str]
    name: Optional[str]
    tag: Optional[str]

class FriendSearchOutput(BaseModel):
    exist_status: bool
    user_data_list: Optional[List[FriendSearchData]] = None
    