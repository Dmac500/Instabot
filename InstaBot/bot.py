from instapy import InstaPy

session = InstaPy(username="email" , password="Password")
session.login()

session.like_by_tags(['ufc'] , amount=6)
session.set_do_follow(True , percentage=100)

session.set_do_comment(True , percentage=50)
session.set_comments(["Lets go", "F in the chat" , "Sick"])

session.end()
