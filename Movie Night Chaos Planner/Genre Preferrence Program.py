Genre = ('Science-friction', 'Horror', 'Superhero', 'Action', 'Adventure', 'Crime-Thriller', 'Comedy', 'Drama', 'Romance', 'Rom-Com', 'Psycological-Thriller')
Friends =['Arka', 'Satish', 'Lakshya', 'Avdoot', 'Swaroop', 'Reetul', 'Shaswhat', 'Spondan', 'Sarthak', 'Jay', 'Pratik', 'Anant', 'Harsh', 'Saptadipa', 'Mahi', 'Shantanu', 'Shalabh', 'Shivanee']
Preferrence = {"Science-friction" : ['Satish', 'Arka', 'Spondan', 'Swaroop'],
              "Horror" : ['Lakshya', 'Arka'],
              "Rom-Com" : ['Reetul', 'Mahi'],
              "Romance" : ['Shaswhat', 'Reetul', 'Shivanee'],
              "Action" : ['Spondan', 'Avdoot', 'Jay', 'Harsh'],
              "Psycological-Thriller" : "Shalabh",
              "Crime-Thriller" : ['Arka', 'Anant'],
              "Comedy" : ['Shivanee', 'Sarthak'],
              "Adventure" : ['Swaroop', 'Saptadipa'],
              "Drama" : ['Pratik', 'Shantanu']}

user_friends = list(map(str, input("Enter the name of you friends: ").split(',')))
print(f"Your friends are: {user_friends}")

for friend in user_friends:
    if friend not in Friends:
        print(f"{friend} is not in the friends list.")
    for genre, friends in Preferrence.items():
        if friend in friends:
            print(f"{friend} likes {genre} genre movies.")

#MAKE SURE YOU TAKE THE INPUT LIKE: Harsh,Jay,Shantanu | THERE SHOULDN'T BE ANY SPACES BETWEEN THE NAMES
#IF YOU TYPE IT LIKE: Harsh, Jay, Shantanu | IT WOULD ONLY GIVE OUTPUT FOR THE FIRST NAME i.e. 'Harsh'



