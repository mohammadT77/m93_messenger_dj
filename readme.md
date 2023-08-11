**Tasks:**

- Design a simple UI
- API: GET chat/ -> returns all chats (with distinct receivers) -> list of receivers
- API: GET chat/messages/ -> returns all messages
- API: GET chat/{receiver_id} -> returns all messages with {receiver_id}
- API: POST chat/{receiver_id} -> create new message from user to receiver_id
- API: DELETE chat/{receiver_id} -> Delete all the messages with receiver
- API: DELETE chat/{receiver_id}/message/{msg_id} -> Delete a specific message