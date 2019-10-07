from rubato_classes import *

def overall_test():
    
    print("Beginning testing...\n")
    
    try:
        test_song_creation()
        test_song_tagging()
        test_database()
        print("\nAll tests complete!!")
        
    except:
        print("TEST FAILED")


def create_song_SoR():
    #create an instance of a song
    f1 = "/Users/ASIMOV/Desktop/Misc./Vaguely Professional/Programming/"
    f2 = "Rubato/Music Files/spiritoftheradio.txt"
    filename = f1+f2
    song1 = SongClass("Spirit of the Radio", "Rush", filename)
    return song1


def create_song_DFtR():
    #create an instance of a song
    f1 = "/Users/ASIMOV/Desktop/Misc./Vaguely Professional/Programming/"
    f2 = "Rubato/Music Files/dontfearthereaper.txt"
    filename = f1+f2
    song2 = SongClass("Don't Fear the Reaper", "Blue Oyster Cult",
                 filename)
    return song2
    

def test_song_creation():
    #create and verify songs were created

    song1 = create_song_SoR()
    song2 = create_song_DFtR()
    song3 = create_song_DFtR()

    assert song1.title == "Spirit of the Radio"
    assert song1.bpm == "und"
    assert song2.artist == "Blue Oyster Cult"
    assert song2.title == song3.title

    assert len(SongClass._all_Songs) == 3

    #verify that each song has a unique ID
    assert song1.id != song2.id
    assert song2.id != song3.id

    print("\tSong Creation test completed!")

    
def test_song_tagging():
    #general test of tagging system
    
    song1 = create_song_SoR()
    song2 = create_song_DFtR()
    
    song1.add_tag("Lyrics Known")
    song2.add_tag("Lyrics Known")
    song1.add_tag("Live")
    song2.add_tag("Interlude")
    song1.add_tag("Favorite")

    #verify tags were correctly added
    assert len(song1.tags) == 3
    assert len(song2.tags) == 2

    #verify the IDs of both songs werte added to the overall tag dictionary
    assert len(SongClass.tags_dictionary["Lyrics Known"]) == 2

    print("\tSong Tagging test completed!")

def test_database():

    #best practice would be to clear out SongClass._all_Songs, but as __del__
    #   is not yet working, that will have to wait.

    song1 = create_song_SoR()
    song2 = create_song_DFtR()
    
    song1.add_tag("Lyrics Known")
    song2.add_tag("Lyrics Known")
    song1.add_tag("Live")
    song2.add_tag("Interlude")
    song1.add_tag("Favorite")

    SongClass.write_to_database()

    print("\tDatabase test complete!")

overall_test()
