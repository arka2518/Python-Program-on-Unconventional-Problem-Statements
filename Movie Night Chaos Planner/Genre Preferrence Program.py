Genre = ('Science-fiction', 'Horror', 'Superhero', 'Action', 'Adventure', 'Crime-Thriller', 'Comedy', 'Drama', 'Romance', 'Rom-Com', 'Psychological-Thriller')
Friends =['Arka', 'Satish', 'Lakshya', 'Avdoot', 'Swaroop', 'Reetul', 'Shaswhat', 'Spondan', 'Sarthak', 'Jay', 'Pratik', 'Anant', 'Harsh', 'Saptadipa', 'Mahi', 'Shantanu', 'Shalabh', 'Shivanee']
Preference = {"Science-fiction" : ['Satish', 'Arka', 'Spondan', 'Swaroop'],
              "Horror" : ['Lakshya', 'Arka'],
              "Superhero" : ['Arka', 'Jay', 'Spondan', 'Satish', 'Lakshya'],
              "Rom-Com" : ['Reetul', 'Mahi'],
              "Romance" : ['Shaswhat', 'Reetul', 'Shivanee'],
              "Action" : ['Spondan', 'Avdoot', 'Jay', 'Harsh'],
              "Psychological-Thriller" : "Shalabh",
              "Crime-Thriller" : ['Arka', 'Anant'],
              "Comedy" : ['Shivanee', 'Sarthak'],
              "Adventure" : ['Swaroop', 'Saptadipa'],
              "Drama" : ['Pratik', 'Shantanu']}

user_friends = list(map(str, input("Enter the name of you friends: ").split(',')))
print(f"Your friends are: {user_friends}")

for friend in user_friends:
    if friend not in Friends:
        print(f"No data of genre available for {friend}.")
    liked_genres = []
    for genre, friends in Preference.items():
        if friend in friends:
            liked_genres.append(genre)
    if liked_genres:
        print(f"{friend} likes {', '.join(liked_genres)} movies.")

#MAKE SURE YOU TAKE THE INPUT LIKE: Harsh,Jay,Shantanu | THERE SHOULDN'T BE ANY SPACES BETWEEN THE NAMES
#IF YOU TYPE IT LIKE: Harsh, Jay, Shantanu | IT WOULD ONLY GIVE OUTPUT FOR THE FIRST NAME i.e. 'Harsh'



