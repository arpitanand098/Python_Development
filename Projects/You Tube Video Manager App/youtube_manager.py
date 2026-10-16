
import json

def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            test = json.load(file)
            # print(type(test))
            return test
    except:
        return []

def helper_data(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)

def list_all_Videos(videos):
       print("\n")
       print("*" * 70)
       for index, video in enumerate(videos, start = 1):
           print(f"{index}. {video['Title']},  Duration: {video['Duration']}")
       print("\n")
       print("*" * 70)
                        
       
def add_video(videos):
    Title = input("Enter Video Title: ")
    Duration = input("Enetr Video Duration: ")
    videos.append({'Title': Title, 'Duration': Duration})
    helper_data(videos)

def update_video(videos):
    list_all_Videos(videos)
    index = int(input("Enter the video number you want to update: "))
    if 1 <= index <= len(videos):
       title =  input("Enter The new video name")
       duration = input("Enter The new video duration")
       videos[index - 1] = {'Title': title, 'Duration': duration }
       helper_data(videos)
    else:
        print("Invalid Index Selected")

def delete_video(videos):
    list_all_Videos(videos)
    index = int(input("Enter the video index you want to delete: "))

    if 1<= index <= len(videos):
        del videos[index -1]
        helper_data(videos)
    else:
        print("Invalid Index Selected")

def main():
    videos = load_data()
    while True:
        print("\n Youtube Manager | Choose Your next Step ")
        print("1. List all youtube Videos ")
        print("2. Add a youtube Video ")
        print("3. Update a youtube video details ")
        print("4. Delete a youtube video ")
        print("5. Exit the App ")
        choice = input("Enter your choice: ")
        # print(videos)

        match choice:
            case '1':
                list_all_Videos(videos)
            case '2':
                add_video(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid Choice")

if __name__ == "__main__":
    main()