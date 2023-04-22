all_users = {}
all_albums = {}

def add_user(username: str, age: int, city: str, albums: list, all_users: dict, all_albums: dict):
    all_users[username]=[age,city,albums]


def add_album(name: str, artist_name: str, genre: str, tracks: int, all_users: dict, all_albums: dict):
    all_albums[name]=[artist_name, genre,tracks]


def query_user_artist(username: str, artist_name: str, all_users: dict, all_albums: dict) -> int:
    s=0
    for i in all_users[username][2]:
        if all_albums[i][0]==artist_name:
            s+=all_albums[i][2]
    return s
        


def query_user_genre(username: str, genre: str, all_users: dict, all_albums: dict) -> int:
    s=0
    for i in all_users[username][2]:
        if all_albums[i][1]==genre:
            s+=all_albums[i][2]
    return s


def query_age_artist(age: int, artist_name: str, all_users: dict, all_albums: dict) -> int:
    s=0
    for i in all_users:
        if all_users[i][0]==age:
            for j in all_users[i][2]:
                if all_albums[j][0]==artist_name:
                    s+=all_albums[j][2]
    return s



def query_age_genre(age: int, genre: str, all_users: dict, all_albums: dict) -> int:
    s=0
    for i in all_users:
        if all_users[i][0]==age:
            for j in all_users[i][2]:
                if all_albums[j][1]==genre:
                    s+=all_albums[j][2]
    return s


def query_city_artist(city: str, artist_name: str, all_users: dict, all_albums: dict) -> int:
    s=0
    for i in all_users:
        if all_users[i][1]==city:
            for j in all_users[i][2]:
                if all_albums[j][0]==artist_name:
                    s+=all_albums[j][2]
    return s


def query_city_genre(city: str, genre: str, all_users: dict, all_albums: dict) -> int:
    s=0
    for i in all_users:
        if all_users[i][1]==city:
            for j in all_users[i][2]:
                if all_albums[j][1]==genre:
                    s+=all_albums[j][2]
    return s

# DO NOT USE YOUR OWN TESTS HERE, USE SAMPLE TEST INSTEAD
