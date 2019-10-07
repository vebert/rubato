'''
TODO:

    write playback
    clean up tag dictionary when deleting song
         iterate over self.tags

'''

import os.path
import csv


class SongClass:
    #the object holding information about the song

    #class variable; dictionary of tags
    #   keys: strings of tag names
    #   values: set of ids of songs using that tag
    
    _unique_id = 0
    _all_Songs = set()
    
    tags_dictionary = dict()
    
    def __init__(self, title, artist, file_pointer):
        self.title = title
        self.artist = artist
        self.bpm = "und"
        self.genre = "und"
        self.rating = "und"
        self.data = file_pointer
        self.validate_data
        self.id = SongClass._unique_id
        SongClass._unique_id += 1
        self.tags = set()
        SongClass._all_Songs.add(self)

        #rewrite database, maybe?
        SongClass.write_to_database()

    
    @classmethod
    def write_to_database(cls):
        #write the information from _all_Songs to a database
        # "Database" at this time means csv

        #at this point, write from scratch every time

        with open("music_informnation_database.csv", mode="w") as csvfile:
            songwriter = csv.writer(csvfile, delimiter = ",")
            
            #write a header, because we're not animals
            header_row = ["Song ID", "Title", "Artist", "Pointer",
                          "Genre", "BPM", "Rating", "Tags"]
            songwriter.writerow(header_row)
            
            for curr_song in SongClass._all_Songs:
                #write the song info

                #first create tags string
                tags_string = "{"
                for tag in curr_song.tags:
                    tags_string += tag + "|"

                #remove the final |, iff any tags exist
                if len(tags_string) == 1:
                    tags_string += "n/a}"
                else:
                    tags_string = tags_string[:-1] + "}"
                
                song_information = [curr_song.id, curr_song.title,
                                    curr_song.artist, curr_song.data,
                                    curr_song.genre, curr_song.bpm,
                                    curr_song.rating, tags_string]
                
                songwriter.writerow(song_information)


    @classmethod
    def read_from_database(cls):
        #read the information from the database to _all_Songs
        #first clear out SongClass._all_Songs, but __del__ is not yet working
        return
        
    def play(self):
        #return the music
        return

    def validate_data(self):
        is_file = os.path.isfile(self.data)
        return is_file

    def add_tag(self, tag):
        
        if not isinstance(tag, str):
            return "Tags must be in the form of a String."

        #add the tag to the specific song's tag set
        self.tags.add(tag)

        #add the tag to the overall Song dictionary
        if tag in self.tags_dictionary:
            #if the tag already exists, add the song's id to the pre-existing
            #set of song ids
            SongClass.tags_dictionary[tag].add(self.id)
        else:
            #add tag to dictionary with set containing only the song id
            SongClass.tags_dictionary[tag] = {self.id}



    #def __del__(self):
        #SongClass._all_Songs.remove(self)
        #TODO: remove from Song tag list

        #redo database
        #SongClass.write_to_database()
    
    
