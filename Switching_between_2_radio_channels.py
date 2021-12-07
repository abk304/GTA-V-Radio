# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 19:29:00 2021

@author: AbhayKaushik
"""
import pygame
import time
from threading import Thread
import random
from pynput import keyboard



def check_switch():
    global channel1
    global channel2
    with keyboard.Events() as events:
        for event in events:
            if event.key == keyboard.Key.space:
                channel1.set_volume(0)
                channel2.set_volume(0.2)
                
            if event.key == keyboard.Key.enter:
                channel1.set_volume(0.2)
                channel2.set_volume(0)
                
                
Thread(target=check_switch).start()
pygame.mixer.init(frequency = 44100, size = -16, channels = 2, buffer = 2**12) 
pygame.mixer.set_num_channels(2)
channel1 = pygame.mixer.Channel(0)
channel2 = pygame.mixer.Channel(1)


non_stop_pop_music_list = ["adult_education", "alright", "anthem", "applause", #Listing all the music in the playable list
              "bad_girls", "cooler_than_me", "days_go_by",
              "dont_wanna_fall_in_love", "everything_she_wants",
              "feel_good_inc", "general", "gimme_more",
              "glamorous", "i_want_it_that_way", "kids",
              "lady_hear_me_tonight", "lets_go_all_the_way",
              "living_in_a_box", "me_and_you",
              "meet_me_halfway", "midnight_city", 
              "moves_like_jagger", "new_sensation", "on_our_own",
              "one_thing", "only_girl_in_the_world", "promises_promises",
              "pure_shores", "rythm_of_the_night", "scandalous",
              "send_me_an_angel", "six_underground", "smalltown_boy",
              "something_got_me_started_remix", "tape_loop",
              "tell_to_my_heart", "tennis_court", "the_time_is_now",
              "time", "to", "wait", "west_end_girls", "with_every_heartbeat",
              "work"]
non_stop_pop_id_list = ["id_01","id_02","id_03","id_04","id_05","id_06", #Listing the ID (intermediate spokens)
           "id_07","id_08","id_09","id_10","id_11","id_12",
           "id_13","id_14","id_15","id_16","id_17"]
non_stop_pop_mono_solo_list = ["mono_solo_01","mono_solo_02", #Listing the mono_solos
                  "mono_solo_03","mono_solo_04",
                  "mono_solo_05","mono_solo_06",
                  "mono_solo_07","mono_solo_08",
                  "mono_solo_09","mono_solo_10",
                  "mono_solo_11","mono_solo_12",
                  "mono_solo_13","mono_solo_14",
                  "mono_solo_15","mono_solo_16",
                  "mono_solo_17","mono_solo_18",
                  "mono_solo_19","mono_solo_20",
                  "mono_solo_21","mono_solo_22",
                  "mono_solo_23","mono_solo_24",
                  "mono_solo_25","mono_solo_26",
                  "mono_solo_27","mono_solo_28",
                  "mono_solo_29"]
non_stop_pop_music_with_preplay_list = ["adult_education", "anthem", "applause", #Listing the music with preplays 
                                  "bad_girls", "cooler_than_me", "days_go_by",
              "dont_wanna_fall_in_love", "everything_she_wants",
              "feel_good_inc", "gimme_more",
              "glamorous", "i_want_it_that_way", "kids",
              "lady_hear_me_tonight", "lets_go_all_the_way",
              "living_in_a_box", "me_and_you",
              "meet_me_halfway", "midnight_city", 
              "moves_like_jagger", "new_sensation", "on_our_own",
              "one_thing", "only_girl_in_the_world", "promises_promises",
              "pure_shores", "rythm_of_the_night", "scandalous",
              "six_underground", "smalltown_boy",
              "something_got_me_started_remix", "tape_loop",
              "tell_to_my_heart", "tennis_court", "the_time_is_now",
              "wait", "west_end_girls", "with_every_heartbeat",
              "work"] 

radio_mirror_park_music_list = ["always", "boogie_in_zero_gravity", "change_of_coast", 
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
radio_mirror_park_id_list = ["id_01","id_02","id_03","id_04","id_05","id_06", #Listing the ID (intermediate spokens)
           "id_07","id_08","id_09","id_10","id_11","id_12",
           "id_13"]
radio_mirror_park_mono_solo_list = ["mono_solo_01","mono_solo_02", #Listing the mono_solos
                  "mono_solo_03","mono_solo_04",
                  "mono_solo_05","mono_solo_06",
                  "mono_solo_07","mono_solo_08",
                  "mono_solo_09","mono_solo_10",
                  "mono_solo_11","mono_solo_12",
                  "mono_solo_13"]
radio_mirror_park_music_with_preplay_list = ["always", "boogie_in_zero_gravity",
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

one_or_two = ["_01", "_02"]

def non_stop_pop():
    while True:
        global channel1
        non_stop_pop_music_track = non_stop_pop_music_list[random.randint(0, len(non_stop_pop_music_list)-1)]
        non_stop_pop_id_track = non_stop_pop_id_list[random.randint(0, len(non_stop_pop_id_list)-1)]
        non_stop_pop_mono_solo_track = non_stop_pop_mono_solo_list[random.randint(0, len(non_stop_pop_mono_solo_list)-1)]
        
        non_stop_pop_music_track_path = "Non Stop Pop Radio\\" + non_stop_pop_music_track + "\\" + non_stop_pop_music_track.upper() + ".wav"
        non_stop_pop_id_track_path = "Non Stop Pop Radio\\" + non_stop_pop_id_track + "\\" + non_stop_pop_id_track.upper() + ".wav"
        non_stop_pop_mono_solo_track_path = "Non Stop Pop Radio\\" + non_stop_pop_mono_solo_track + "\\" + non_stop_pop_mono_solo_track.upper() + ".wav"
        
        non_stop_pop_music_track_sound = pygame.mixer.Sound(non_stop_pop_music_track_path)
        non_stop_pop_id_track_sound = pygame.mixer.Sound(non_stop_pop_id_track_path)
        non_stop_pop_mono_solo_track_sound = pygame.mixer.Sound(non_stop_pop_mono_solo_track_path)
        
        if non_stop_pop_music_track in non_stop_pop_music_with_preplay_list:
            non_stop_pop_preplay_track = non_stop_pop_music_track + one_or_two[random.randint(0, 1)]
            non_stop_pop_preplay_track_path = "Non Stop Pop Radio\\" + "intro\\" + non_stop_pop_preplay_track.upper() + ".wav"
            non_stop_pop_preplay_track_sound = pygame.mixer.Sound(non_stop_pop_preplay_track_path)
            
            if random.randint(0,1) == 0:
                channel1.play(non_stop_pop_mono_solo_track_sound)
                time.sleep(non_stop_pop_mono_solo_track_sound.get_length())
                channel1.play(non_stop_pop_id_track_sound)
                time.sleep(non_stop_pop_id_track_sound.get_length())
                channel1.play(non_stop_pop_music_track_sound)
                time.sleep(non_stop_pop_music_track_sound.get_length())
            elif random.randint(0, 1) == 1:
                channel1.play(non_stop_pop_mono_solo_track_sound)
                time.sleep(non_stop_pop_mono_solo_track_sound.get_length())
                channel1.play(non_stop_pop_preplay_track_sound)
                time.sleep(non_stop_pop_preplay_track_sound.get_length())
                channel1.play(non_stop_pop_music_track_sound)
                time.sleep(non_stop_pop_music_track_sound.get_length())

                
def radio_mirror_park():
    while True:
        global channel2
        radio_mirror_park_music_track = radio_mirror_park_music_list[random.randint(0, len(radio_mirror_park_music_list)-1)]
        radio_mirror_park_id_track = radio_mirror_park_id_list[random.randint(0, len(radio_mirror_park_id_list)-1)]
        radio_mirror_park_mono_solo_track = radio_mirror_park_mono_solo_list[random.randint(0, len(radio_mirror_park_mono_solo_list)-1)]
        
        radio_mirror_park_music_track_path = "Radio Mirror Park\\" + radio_mirror_park_music_track + "\\" + radio_mirror_park_music_track.upper() + ".wav"
        radio_mirror_park_id_track_path = "Radio Mirror Park\\" + radio_mirror_park_id_track + "\\" + radio_mirror_park_id_track.upper() + ".wav"
        radio_mirror_park_mono_solo_track_path = "Radio Mirror Park\\" + radio_mirror_park_mono_solo_track + "\\" + radio_mirror_park_mono_solo_track.upper() + ".wav"
        
        radio_mirror_park_music_track_sound = pygame.mixer.Sound(radio_mirror_park_music_track_path)
        radio_mirror_park_id_track_sound = pygame.mixer.Sound(radio_mirror_park_id_track_path)
        radio_mirror_park_mono_solo_track_sound = pygame.mixer.Sound(radio_mirror_park_mono_solo_track_path)
        
        if radio_mirror_park_music_track in radio_mirror_park_music_with_preplay_list:
            radio_mirror_park_preplay_track = radio_mirror_park_music_track + one_or_two[random.randint(0, 1)]
            radio_mirror_park_preplay_track_path = "Radio Mirror Park\\" + "intro\\" + radio_mirror_park_preplay_track.upper() + ".wav"
            radio_mirror_park_preplay_track_sound = pygame.mixer.Sound(radio_mirror_park_preplay_track_path)
            
            
            if random.randint(0,1) == 0:
                channel2.play(radio_mirror_park_mono_solo_track_sound)
                time.sleep(radio_mirror_park_mono_solo_track_sound.get_length())
                channel2.play(radio_mirror_park_id_track_sound)
                time.sleep(radio_mirror_park_id_track_sound.get_length())
                channel2.play(radio_mirror_park_music_track_sound)
                time.sleep(radio_mirror_park_music_track_sound.get_length())
            elif random.randint(0, 1) == 1:
                channel2.play(radio_mirror_park_mono_solo_track_sound)
                time.sleep(radio_mirror_park_mono_solo_track_sound.get_length())
                channel2.play(radio_mirror_park_preplay_track_sound)
                time.sleep(radio_mirror_park_preplay_track_sound.get_length())
                channel2.play(radio_mirror_park_music_track_sound)
                time.sleep(radio_mirror_park_music_track_sound.get_length())
                
channel1.set_volume(0)
channel2.set_volume(0.2)
 
if __name__ == '__main__':
    Thread(target=non_stop_pop).start()
    Thread(target=radio_mirror_park).start()

check_switch()   


  
 
    
 
  

     

     
     
 
 
 
 
 
 
 
  
          


         
        
       
         
       
         
       
        
       
        
        
         