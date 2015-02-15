# lfm - the last.fm player

A last.fm based playlist creator.

`lfm update` - Create or Update your local database of music files.

`lfm diff [me] users` - Find differences in music taste between users.

`lfm common [me] [users]` - Find stuff common between users.

`lfm play [--artist | --user]` - Generate and Play a playlist for an artist/user.

`lfm scrobbles [users] [--plot]` - List or plot number of scrobbles for users.

### Sample CLI Calls

`lfm play --artist "Kings of Leon" --top 20` - Play top 20 tracks of KOL 
(present in your library).

`lfm play --user nickedes --loved` - Play all loved tracks of nickedes.

`lfm play --user nickedes` - Play last played tracks of nickedes.

`lfm play --charts --region India` - Play stuff thats hot on Indian charts.

`lfm play --never-played` - Play stuff from my library that I've never scrobbled.

`lfm common nickedes trigonaminima | lfm play` - Listen to songs that both nickedes and trigonaminima like.

`lfm diff --artists nickedes trigonaminima` - List artists that only one of nickedes and minima listen. (side by side diff? genres?)

### Steps

Create a SQLite database of user's entire music collection (take in a list of directories and recurse all of them.)

Use [`stagger`](https://code.google.com/p/stagger/) to extract metadata from the music files.

Use `Clink` to create a sane command line interface.

Think about how you'll find `diff`.

### Database Schema

`Users`, `Artist`, `Albums`, `Songs`.