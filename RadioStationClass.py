# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 23:41:21 2021

@author: AbhayKaushik
"""

import random 
import pygame
from time import sleep
from pynput import keyboard
from threading import Thread 


pygame.mixer.init(frequency = 44100, size = -16, channels = 4, buffer = 2**12) 
pygame.mixer.set_num_channels(4)
channel1 = pygame.mixer.Channel(0)
channel2 = pygame.mixer.Channel(1)
channel3 = pygame.mixer.Channel(2)
channel4 = pygame.mixer.Channel(3)

def check_switch():
    global channel1
    global channel2
    global channel3
    with keyboard.Events() as events:
        for event in events:
            if event.key == keyboard.Key.enter:
                radio_mirror_park.channel.set_volume(0.1)
                non_stop_pop.channel.set_volume(0)
                los_santos_rock.channel.set_volume(0)
                rebel_radio.channel.set_volume(0)
            if event.key == keyboard.Key.space:
                radio_mirror_park.channel.set_volume(0)
                non_stop_pop.channel.set_volume(0.1)
                los_santos_rock.channel.set_volume(0)
                rebel_radio.channel.set_volume(0)
            if event.key == keyboard.Key.esc:
                radio_mirror_park.channel.set_volume(0)
                non_stop_pop.channel.set_volume(0)
                los_santos_rock.channel.set_volume(0.1)
                rebel_radio.channel.set_volume(0)
            if event.key == keyboard.Key.ctrl_l:
                radio_mirror_park.channel.set_volume(0)
                non_stop_pop.channel.set_volume(0)
                los_santos_rock.channel.set_volume(0)
                rebel_radio.channel.set_volume(0.1)

Thread(target=check_switch).start()

class RadioStation:
    
    station_count = 0
    
    def __init__(self, name, music_list, id_list, mono_solo_list, music_with_preplay_list, channel):
        self.name = name
        self.music_list = music_list
        self.id_list = id_list
        self.mono_solo_list = mono_solo_list
        self.music_with_preplay_list = music_with_preplay_list
        self.channel = channel
        RadioStation.station_count += 1
        
    def displayCount(self):
        print ("Total stations = %d" % RadioStation.station_count)
    def displayStation(self):
        print ("Station name: ", self.name)
    def trackCount(self):
        print(self.displayStation(), 
              "Number of music tracks: %d" % len(self.music_list), "\n",
              "Number of ID tracks: %d" % len(self.id_list), "\n",
              "Number of MonoSolo tracks: %d" % len(self.mono_solo_list), "\n",
              "Number of music tracks with preplay: %d" % len(self.music_with_preplay_list))
        
    def playMusic(self):
        current_track = self.music_list[random.randint(0,len(self.music_list) - 1)]
        current_track_path = self.name + "\\" + current_track + "\\" + current_track.upper() + ".wav"
        current_track_sound = pygame.mixer.Sound(current_track_path)
        self.channel.set_volume(0)
        self.channel.play(current_track_sound)
        print("Now playing...")
        #sleep(current_track_sound.get_length())

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
   
los_santos_rock_music_list = ["all_the_things_she_said", "baker_street", "big_log", 
              "black_velvet", #Listing all the music in the playable list
              "burning_heart", "carry_on_my_wayward_sun", "cats_in_the_cradle",
              "circle_in_the_sand", "coming_on_strong",
              "danger_zone", "dirty_white_boy", "fortunate_son",
              "general", "gimme_all_your_lovin", "heartbeat",
              "higher_love", "hollywood_nights",
              "i_cant_wait", "i_dont_care_anymore",
              "i_wouldnt_want_to_be", "if_you_leave_me_now", 
              "im_free", "lonely_is_the_night", "mississippi_queen",
              "night_moves", "ogdens_nut_gone_flake", "peace_of_mind",
              "photograph", "radio_ga_ga", "rain",
              "rockin_me", "roundabout", "saturday_nights_alright",
              "shadows_of_the_night", "the_breakup_song",
              "thirty_days_in_the_hole", "time", "to",
              "too_late_for_goodbyes", "we_built_this_city",
              "what_a_fool_believes"]
los_santos_rock_id_list = ["id_01","id_02","id_03","id_04","id_05","id_06", #Listing the ID (intermediate spokens)
           "id_07","id_08","id_09","id_10","id_11","id_12",
           "id_13"]
los_santos_rock_mono_solo_list = ["mono_solo_01","mono_solo_02", #Listing the mono_solos
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
                  "mono_solo_25"]
los_santos_rock_music_with_preplay_list = ["all_the_things_she_said", "baker_street", "big_log", 
              "black_velvet", #Listing all the music in the playable list
              "burning_heart", "carry_on_my_wayward_sun", "cats_in_the_cradle",
              "coming_on_strong",
              "dirty_white_boy", "fortunate_son",
              "gimme_all_your_lovin", "heartbeat",
              "higher_love", "hollywood_nights",
              "i_cant_wait", 
              "i_wouldnt_want_to_be", "if_you_leave_me_now", 
              "im_free", "lonely_is_the_night", "mississippi_queen",
              "night_moves", "ogdens_nut_gone_flake", "peace_of_mind",
              "photograph", "radio_ga_ga", "rain",
              "roundabout", "saturday_nights_alright",
              "shadows_of_the_night", "the_breakup_song",
              "thirty_days_in_the_hole",
              "too_late_for_goodbyes", "we_built_this_city",
              "what_a_fool_believes"]
 
rebel_radio_music_list = ["are_you_sure_hank", "cant_hardly_stand", "convoy",
                          "crazy_arms", "dippin_snuff", "divorce", "general",
                          "get_outta_my_car", "get_with_it", "highway_man",
                          "i_aint_living_long_like_this", "if_want_to_get_heaven",
                          "intro", "it_dont_hurt_anymore", "it_wont_be_long_hating_you",
                          "she_made_toothpicks_out_of_me", "the_general_lee",
                          "time", "to", "whiskey_river", "you_took_all_the_ramblin_out"]
rebel_radio_id_list = ["id_01", "id_02", "id_03", "id_04", "id_05", "id_06",
                       "id_07", "id_08", "id_09", "id_10", "id_11", "id_12",
                       "id_13"]
rebel_radio_mono_solo_list = ["mono_solo_01", "mono_solo_02", "mono_solo_03",
                              "mono_solo_04", "mono_solo_05", "mono_solo_06",
                              "mono_solo_07", "mono_solo_08", "mono_solo_09",
                              "mono_solo_10", "mono_solo_11", "mono_solo_12",
                              "mono_solo_13", "mono_solo_14", "mono_solo_15",
                              "mono_solo_16", "mono_solo_17", "mono_solo_18",
                              "mono_solo_19", "mono_solo_20", "mono_solo_21"]
rebel_radio_music_with_preplay_list = ["are_you_sure_hank", "cant_hardly_stand",
                                       "convoy", "get_outta_my_car", "i_aint_living_long_like_this",
                                       "if_want_to_get_heaven", "it_dont_hurt_anymore",
                                       "it_wont_be_long_hating_you", "the_general_lee",
                                       "whiskey_river", "you_took_all_the_ramblin_out"]


non_stop_pop = RadioStation("Non Stop Pop Radio", non_stop_pop_music_list, 
                            non_stop_pop_id_list, non_stop_pop_mono_solo_list, 
                            non_stop_pop_music_with_preplay_list, channel1)
radio_mirror_park = RadioStation("Radio Mirror Park", radio_mirror_park_music_list, 
                                 radio_mirror_park_id_list, radio_mirror_park_mono_solo_list, 
                                 radio_mirror_park_music_with_preplay_list, channel2)
los_santos_rock = RadioStation("Los Santos Rock Radio", los_santos_rock_music_list, 
                               los_santos_rock_id_list, los_santos_rock_mono_solo_list, 
                               los_santos_rock_music_with_preplay_list, channel3)
rebel_radio = RadioStation("Rebel Radio", rebel_radio_music_list, rebel_radio_id_list,
                           rebel_radio_mono_solo_list,rebel_radio_music_with_preplay_list, 
                           channel4)

stations = [non_stop_pop, radio_mirror_park, los_santos_rock]
    
radio_mirror_park.trackCount()
non_stop_pop.trackCount()
los_santos_rock.trackCount()
rebel_radio.trackCount()

radio_mirror_park.channel.set_volume(0)
non_stop_pop.channel.set_volume(0)
los_santos_rock.channel.set_volume(0)
rebel_radio.channel.set_volume(0)


if __name__ == '__main__':
    p1 = Thread(target=radio_mirror_park.playMusic)
    p2 = Thread(target=non_stop_pop.playMusic)
    p3 = Thread(target=los_santos_rock.playMusic)
    p4 = Thread(target=rebel_radio.playMusic)
    p1.start()
    p2.start()
    p3.start()
    p4.start()

check_switch()
