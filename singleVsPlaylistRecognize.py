
# Playlist Link:
# https://www.youtube.com/playlist?list=PLMyBqE0aQxbnwkBegz0g096c-JfescfRX
# 
# Video Link:
# https://www.youtube.com/watch?v=69TsvM_Vax8&list=PLMyBqE0aQxbnwkBegz0g096c-JfescfRX
# https://www.youtube.com/watch?v=bOEZBW5N6EA
user_input = input("Enter either a video link or a playlist link: ")

print(f"The input is: {user_input}")

if "playlist" in user_input:
    print("This is a playlist link!")
elif "watch" in user_input:
    print("This is a normal video!")
else:
    print("This is neither one!")
