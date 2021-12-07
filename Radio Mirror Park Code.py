# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 09:59:22 2021

@author: AbhayKaushik
"""

"""Creating a single radio station for GTA V radio :)"""
from playsound import playsound
import keyboard 
import random
# This will be Radio Mirror Park

music_list = ["always", "boogie_in_zero_gravity", "change_of_coast", 
              "colours", #Listing all the music in the playable list
              "crystalfilm", "dark_matter", "do_you_believe",
              "dont_come_close", "feel_the_same",
              "flutes", "forget", "from_nowhere",
              "general", "heart_in_the_pipes", "heartbreak",
              "high_pressure", "hold_on_holy_ghost",
              "in_real_life", "jasmine",
              "little_white_lie", "living_in_america", 
              "lucky_boy", "mesmerized", "nowhere_to_go",
              "new_beat", "o_n_e", "old_love",
              "one_girl_one_boy", "pharaohs", "polish_girl",
              "psychic_city", "shine_a_light", "shooting_holes",
              "sleepwalking", "so_many_details",
              "sometimes", "strangers_in_the_wind", "the_drummer",
              "the_set_up", "time", "to", "truly_alive",
              "when_youre_out"]
id_list = ["id_01","id_02","id_03","id_04","id_05","id_06", #Listing the ID (intermediate spokens)
           "id_07","id_08","id_09","id_10","id_11","id_12",
           "id_13"]
mono_solo_list = ["mono_solo_01","mono_solo_02", #Listing the mono_solos
                  "mono_solo_03","mono_solo_04",
                  "mono_solo_05","mono_solo_06",
                  "mono_solo_07","mono_solo_08",
                  "mono_solo_09","mono_solo_10",
                  "mono_solo_11","mono_solo_12",
                  "mono_solo_13"]
music_with_preplay_list = ["always", "boogie_in_zero_gravity",
               #Listing all the music in the playable list
              "crystalfilm", "dark_matter", "do_you_believe",
              "dont_come_close", "feel_the_same",
              "forget", "from_nowhere",
              "heart_in_the_pipes", 
              "hold_on_holy_ghost",
              "in_real_life", "jasmine",
              "little_white_lie", "living_in_america", 
              "lucky_boy", "nowhere_to_go",
              "new_beat", "old_love",
              "one_girl_one_boy", "polish_girl",
              "psychic_city", "shine_a_light", "shooting_holes",
              "sleepwalking", "so_many_details",
              "sometimes", "the_drummer",
              "truly_alive",
              "when_youre_out"]
#preplay_list = ["adult_education_01","adult_education_02", #List of music preplays
#              "anthem_01", "anthem_02", "applause_01", "applause_02",
#              "bad_girls_01", "bad_girls_02", "cooler_than_me_01", "cooler_than_me_02",
#              "days_go_by_01", "days_go_by_02"
#              "dont_wanna_fall_in_love_01", "dont_wanna_fall_in_love_02",
#              "everything_she_wants_01", "everything_she_wants_02",
#              "feel_good_inc_01", "feel_good_inc_02", "gimme_more_01", "gimme_more_02",
#              "glamorous_01", "glamorous_02", "i_want_it_that_way_01",
#              "i_want_it_that_way_02", "kids_01", "kids_02",
#              "lady_hear_me_tonight_01", "lady_hear_me_tonight_02",
#              "lets_go_all_the_way_01", "lets_go_all_the_way_02"
#              "living_in_a_box_01", "living_in_a_box_02", "me_and_you_01",
#              "me_and_you_02", 
#              "meet_me_halfway_01", "meet_me_halfway_02", "midnight_city_01",
#              "midnight_city_02", 
#              "moves_like_jagger_01", "moves_like_jagger_02", "new_sensation_01",
#              "new_sensation_02", "on_our_own_01", "on_our_own_02",
#              "one_thing_01", "one_thing_02", "only_girl_in_the_world_01",
#              "only_girl_in_the_world_02", "promises_promises_01", "promises_promises_02",
#              "pure_shores_01", "pure_shores_02", "rythm_of_the_night_01", 
#              "rythm_of_the_night_02", "scandalous_01", "scandalous_02",
#              "six_underground_01", "six_underground_02", "smalltown_boy_01", "smalltown_boy_02",
#              "something_got_me_started_remix_01","something_got_me_started_remix_02" , 
#              "tape_loop_01", "tape_loop_02",
#              "tennis_court_01", "tennis_court_02", "the_time_is_now_01", "the_time_is_now_02",
#              "wait_01", "wait_02", "west_end_girls_01", "west_end_girls_02", 
#              "with_every_heartbeat_01", "with_every_heartbeat_02",
#              "work_01", "work_02"]

one_or_two = ["_01", "_02"]

music_list_length = len(music_list) #Length of music list
id_list_length = len(id_list) #Length of ID list
mono_solo_list_length = len(mono_solo_list) #Length of mono solo list

def play_track(): #Function plays random tracks
    current_music_track = music_list[random.randint(0,music_list_length-1)] #Pick random music track
    current_id_track = id_list[random.randint(0, id_list_length-1)] #Pick random id
    current_mono_solo_track = mono_solo_list[random.randint(0, mono_solo_list_length-1)] #Pick random mono solo
    
    if current_music_track in music_with_preplay_list: #Checking if music has a preplay track
        current_preplay_track = current_music_track + one_or_two[random.randint(0,1)] #If it does, select any one of the 2 available
        preplay_track_path = "intro\\" + current_preplay_track.upper() + ".wav"  #Creating track path
    
    music_track_path = current_music_track + "\\" +current_music_track.upper()+".wav" #Creating music track path
    id_track_path = current_id_track + "\\" +current_id_track.upper()+".wav" #Creating id track path
    mono_solo_track_path = current_mono_solo_track + "\\" +current_mono_solo_track.upper()+".wav" #Creating mono solo track path
    
    #Picking if the preplay will play or just an id
    if random.randint(0, 1) == 0: #Do not play preplay, play id
        playsound(mono_solo_track_path)
        playsound(id_track_path)
        playsound(music_track_path)
    elif random.randint(0, 1) == 1: #Play preplay, do not play id
        playsound(mono_solo_track_path)
        playsound(preplay_track_path)
        playsound(music_track_path)


while True and not keyboard.is_pressed('`'): #Execute forever
    play_track() #Execute function
    