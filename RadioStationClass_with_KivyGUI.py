# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 10:24:00 2021

@author: AbhayKaushik
"""

#Implementing RADIO Audio backend and GUI with KIVY
#All audio code snippets are between equal sign barriers

import random
import pygame
import time
from threading import Thread


from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.config import Config
from kivy.core.text import LabelBase
from kivy.clock import Clock

#Creating the font for UI
LabelBase.register(name='CL1960', fn_regular='Chalet London Nineteen Sixty Font.ttf')
LabelBase.register(name='CNY1960', fn_regular='Chalet New York Nineteen Sixty Font.ttf')

#============================================
pygame.mixer.init(frequency = 44100, size = -16, channels = 5, buffer = 2**12) 
pygame.mixer.set_num_channels(5)
channel1 = pygame.mixer.Channel(0)
channel2 = pygame.mixer.Channel(1)
channel3 = pygame.mixer.Channel(2)
channel4 = pygame.mixer.Channel(3)
channel5 = pygame.mixer.Channel(4)

def KillRadio():
    channel1.set_volume(0)
    channel2.set_volume(0)
    channel3.set_volume(0)
    channel4.set_volume(0)
    channel5.set_volume(0)
    pygame.mixer.stop()
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()
    
#=============================================

global index
index=0

#Next, define check_switch that checks if user switched radio stations
def check_switch():
    global channel1
    global channel2
    global channel3
    global channel4
    global index
    
    if index == 0:
        channel1.set_volume(0.1)
        channel2.set_volume(0)
        channel3.set_volume(0)
        channel4.set_volume(0)
        channel5.set_volume(0)
    if index == 1:
        channel1.set_volume(0)
        channel2.set_volume(0.1)
        channel3.set_volume(0)
        channel4.set_volume(0)
        channel5.set_volume(0)
    if index == 2:
        channel1.set_volume(0)
        channel2.set_volume(0)
        channel3.set_volume(0.1)
        channel4.set_volume(0)
        channel5.set_volume(0)
    if index == 3:
        channel1.set_volume(0)
        channel2.set_volume(0)
        channel3.set_volume(0)
        channel4.set_volume(0.1)
        channel5.set_volume(0)
    if index == 4:
        channel1.set_volume(0)
        channel2.set_volume(0)
        channel3.set_volume(0)
        channel4.set_volume(0)
        channel5.set_volume(0.1)

Thread(target=check_switch).start()

#=====================================
#Next, defining RadioStation class, defining the music lists and
#defining starting tracks as well as station objects
one_or_two_or_three = ["_01"]#, "_02"] #Some tracks have 3 possible intros, add it in later

class RadioStation:
    
    station_count = 0
    
    def __init__(self, name, music_list, id_list, mono_solo_list, music_with_preplay_list, channel, current_music_track, current_track, GUI_index):
        self.name = name
        self.music_list = music_list
        self.id_list = id_list
        self.mono_solo_list = mono_solo_list
        self.music_with_preplay_list = music_with_preplay_list
        self.channel = channel
        self.current_music_track = current_music_track
        self.current_track = current_track
        self.GUI_index = GUI_index
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
        #current_music_track = self.music_list[random.randint(0,len(self.music_list) - 1)]
        current_music_track_v = self.current_music_track
        self.current_track = current_music_track_v
        current_music_track_v = str(current_music_track_v)
        current_music_track_path = self.name + "\\" + current_music_track_v + "\\" + current_music_track_v.upper() + ".wav"
        current_music_track_sound = pygame.mixer.Sound(current_music_track_path)
        self.channel.play(current_music_track_sound)
        #print("Now playing...")
        
        time.sleep(current_music_track_sound.get_length())
        
        self.current_music_track = self.music_list[random.randint(0, len(self.music_list) - 1)] 
        
    def playID(self):
        current_id_track = self.id_list[random.randint(0, len(self.id_list)-1)]
        self.current_track = current_id_track
        current_id_track_path = self.name + "\\" + current_id_track + "\\" + current_id_track.upper() + ".wav"
        current_id_track_sound = pygame.mixer.Sound(current_id_track_path)
        self.channel.play(current_id_track_sound)
        
        time.sleep(current_id_track_sound.get_length())
        
    def playMonoSolo(self):
        current_MS_track = self.mono_solo_list[random.randint(0, len(self.mono_solo_list)-1)]
        self.current_track = current_MS_track
        current_MS_track_path = self.name + "\\" + current_MS_track + "\\" + current_MS_track.upper() + ".wav"
        current_MS_track_sound = pygame.mixer.Sound(current_MS_track_path)
        self.channel.play(current_MS_track_sound)
        
        time.sleep(current_MS_track_sound.get_length())
        
    def playPreplayTrack(self): #preplay track selects the track to play since it cannot handle the "None" object arg before song is selected to play
        #self.current_track = self.music_with_preplay_list[random.randint(0,len(self.music_with_preplay_list) - 1)]
        current_preplay_track = self.current_music_track
        self.current_track = current_preplay_track
        current_preplay_track = str(current_preplay_track)
        current_preplay_track_path = self.name + "\\intro\\" + current_preplay_track.upper() + one_or_two_or_three[0] + ".wav"
        current_preplay_track_sound = pygame.mixer.Sound(current_preplay_track_path)
        self.channel.play(current_preplay_track_sound)
        
        time.sleep(current_preplay_track_sound.get_length())
        
    def playOneRadioCycle_infinite(self):
        while True:
            rng_zero_or_one = random.randint(0, 1)
            self.playMonoSolo()
            if rng_zero_or_one == 0 and self.current_music_track in self.music_with_preplay_list:
                self.playPreplayTrack()
            else:
                self.playID()
            self.playMusic()
    

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
              "west_end_girls", "with_every_heartbeat",
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
              "flutes", "forget", "from_nowhere","heart_in_the_pipes", "heartbreak",
              "high_pressure", "hold_on_holy_ghost",
              "in_real_life", "jasmine",
              "little_white_lie", "living_in_america", 
              "lucky_boy", "mesmerized", "nowhere_to_go",
              "new_beat", "o_n_e", "old_love",
              "one_girl_one_boy", "pharaohs", "polish_girl",
              "psychic_city", "shine_a_light", "shooting_holes",
              "sleepwalking", "so_many_details",
              "sometimes", "strangers_in_the_wind", "the_drummer",
              "the_set_up", "truly_alive",
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
              "gimme_all_your_lovin", "heartbeat",
              "higher_love", "hollywood_nights",
              "i_cant_wait", "i_dont_care_anymore",
              "i_wouldnt_want_to_be", "if_you_leave_me_now", 
              "im_free", "lonely_is_the_night", "mississippi_queen",
              "night_moves", "ogdens_nut_gone_flake", "peace_of_mind",
              "photograph", "radio_ga_ga", "rain",
              "rockin_me", "roundabout", "saturday_nights_alright",
              "shadows_of_the_night", "the_breakup_song",
              "thirty_days_in_the_hole",
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
                          "crazy_arms", "dippin_snuff", "divorce",
                          "get_outta_my_car", "get_with_it", "highway_man",
                          "i_aint_living_long_like_this", "if_want_to_get_heaven",
                          "it_dont_hurt_anymore", "it_wont_be_long_hating_you",
                          "she_made_toothpicks_out_of_me", "the_general_lee",
                          "whiskey_river", "you_took_all_the_ramblin_out"]
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

radio_los_santos_music_list = ["adhd", "ali_bomaye", "bad_news", "bassheads", "bugatti",
                               "collard_greens", "do_it_big", "easily", "everyday", "hold_up",
                               "hood_gone_love_it", "how_it_was", "hunnid_stax", "i_cant_wait_scooter",
                               "illuminate", "im_a_real_one", "kush_coma", "life_of_a_mack", "millions",
                               "r_cali", "relaxin", "say_that_then", "sellin_dope", "slow_down",
                               "smokin_and_ridin", "still_livin", "swimming_pools", "too_hood",
                               "upper_echelon", "work_ferg", "work_young_scooter"] #use hiphop new for this
radio_los_santos_id_list = ["id_01", "id_02",
                            "id_03", "id_04",
                            "id_05", "id_06",
                            "id_07", "id_08",
                            "id_09", "id_10",
                            "id_11", "id_12",
                            "id_13", "id_14"]
radio_los_santos_mono_solo_list = ["mono_solo_01", "mono_solo_02",
                                   "mono_solo_03", "mono_solo_04",
                                   "mono_solo_05", "mono_solo_06",
                                   "mono_solo_07", "mono_solo_08",
                                   "mono_solo_09", "mono_solo_10",
                                   "mono_solo_11", "mono_solo_12",
                                   "mono_solo_13", "mono_solo_14",
                                   "mono_solo_15", "mono_solo_16",
                                   "mono_solo_17", "mono_solo_18",
                                   "mono_solo_19", "mono_solo_20",
                                   "mono_solo_21"]
radio_los_santos_music_with_preplay_list = ["adhd", "ali_bomaye", "bad_news", "bassheads", "bugatti",
                               "collard_greens", "do_it_big", "easily", "everyday",
                               "hood_gone_love_it", "how_it_was", "hunnid_stax", "i_cant_wait_scooter",
                               "illuminate", "im_a_real_one", "kush_coma", "life_of_a_mack", "millions",
                               "r_cali", "relaxin", "say_that_then", "slow_down",
                               "smokin_and_ridin", "still_livin", "swimming_pools", "too_hood",
                               "upper_echelon", "work_ferg", "work_young_scooter"]

non_stop_pop_start_track = non_stop_pop_music_list[random.randint(0, len(non_stop_pop_music_list)-1)]
radio_mirror_park_start_track = radio_mirror_park_music_list[random.randint(0, len(radio_mirror_park_music_list)-1)]
los_santos_rock_start_track = los_santos_rock_music_list[random.randint(0, len(los_santos_rock_music_list)-1)]
rebel_radio_start_track = rebel_radio_music_list[random.randint(0, len(rebel_radio_music_list)-1)]
radio_los_santos_start_track = radio_los_santos_music_list[random.randint(0, len(radio_los_santos_music_list)-1)]


non_stop_pop = RadioStation("Non Stop Pop Radio", non_stop_pop_music_list, 
                            non_stop_pop_id_list, non_stop_pop_mono_solo_list, 
                            non_stop_pop_music_with_preplay_list, channel1, 
                            non_stop_pop_start_track, "", GUI_index=0)
radio_mirror_park = RadioStation("Radio Mirror Park", radio_mirror_park_music_list, 
                                 radio_mirror_park_id_list, radio_mirror_park_mono_solo_list, 
                                 radio_mirror_park_music_with_preplay_list, channel2, 
                                 radio_mirror_park_start_track, "", GUI_index=1)
los_santos_rock = RadioStation("Los Santos Rock Radio", los_santos_rock_music_list, 
                               los_santos_rock_id_list, los_santos_rock_mono_solo_list, 
                               los_santos_rock_music_with_preplay_list, channel3, 
                               los_santos_rock_start_track, "", GUI_index=2)
rebel_radio = RadioStation("Rebel Radio", rebel_radio_music_list, rebel_radio_id_list,
                           rebel_radio_mono_solo_list,rebel_radio_music_with_preplay_list, 
                           channel4, rebel_radio_start_track, "", GUI_index=3)
radio_los_santos = RadioStation("Radio Los Santos", radio_los_santos_music_list, radio_los_santos_id_list,
                           radio_los_santos_mono_solo_list, radio_los_santos_music_with_preplay_list, 
                           channel5, radio_los_santos_start_track, "", GUI_index=4)

stationList = [non_stop_pop, radio_mirror_park, 
               los_santos_rock, rebel_radio,
               radio_los_santos]
#===============================================

#===============================================
#Initializing all channels to be mute
radio_mirror_park.channel.set_volume(0)
non_stop_pop.channel.set_volume(0)
los_santos_rock.channel.set_volume(0)
rebel_radio.channel.set_volume(0)
radio_los_santos.channel.set_volume(0)
#===============================================

Config.set('graphics', 'width', '960')
Config.set('graphics', 'height', '540')
Config.set('graphics', 'resizable', False)

from kivy.core.window import Window 
Window.clearcolor=(22/255,35/255,64/255,1)

NonStopPopLogo = Image(source='Non Stop Pop Logo.png',pos=(290,115),size_hint=(0.4,0.4))
RadioMirrorParkLogo = Image(source='Radio Mirror Park Logo.png',pos=(290,115),size_hint=(0.4,0.4))
LosSantosRockRadioLogo = Image(source='Los Santos Rock Radio Logo.png',pos=(290,115),size_hint=(0.4,0.4))
RebelRadioLogo = Image(source='Rebel Radio Logo.png',pos=(290,115),size_hint=(0.4,0.4))
RadioLosSantosLogo = Image(source='Radio Los Santos Logo.png',pos=(290,115),size_hint=(0.4,0.4))

NonStopPopLabel = Label(text="Non Stop Pop", pos=(0,100), font_size = '60sp', bold = True, font_name="CNY1960")
RadioMirrorParkLabel = Label(text="Radio Mirror Park", pos=(0,100), font_size = '60sp', bold = True, font_name="CNY1960")
LosSantosRockRadioLabel = Label(text="Los Santos Rock Radio", pos=(0,100), font_size = '60sp', bold = True, font_name="CNY1960")
RebelRadioLabel = Label(text="Rebel Radio", pos=(0,100), font_size = '60sp', bold = True, font_name="CNY1960")
RadioLosSantosLabel = Label(text="Radio Los Santos", pos=(0,100), font_size = '60sp', bold = True, font_name="CNY1960")

global MusicNameLabel
MusicNameLabel = Label(text="", pos=(0,0), font_size = '30sp', bold = True, font_name = "CL1960")

global Images
Images = [NonStopPopLogo, RadioMirrorParkLogo,
          LosSantosRockRadioLogo, RebelRadioLogo,
          RadioLosSantosLogo]
global StationLabelNames
StationLabelNames = [NonStopPopLabel, RadioMirrorParkLabel,
                     LosSantosRockRadioLabel, RebelRadioLabel,
                     RadioLosSantosLabel]
global MusicName
MusicName = ""


def leftStation(instance):
    global index
    global Images
    global MusicNameLabel
    layout.remove_widget(Images[index])
    layout.remove_widget(StationLabelNames[index])
    layout.remove_widget(MusicNameLabel)
    
    index = index - 1
    if index < 0:
        index = len(Images)-1
    
    check_switch()
    layout.add_widget(Images[index])
    layout.add_widget(StationLabelNames[index])
    
    if stationList[index].current_track in stationList[index].music_list:
        MusicName = stationList[index].current_music_track.upper()
        MusicName = MusicName.replace("_", " ")
        MusicNameLabel = Label(text=MusicName, pos=(0,-150), font_size = '30sp', bold = True, font_name = "CL1960")
        layout.add_widget(MusicNameLabel)
        
    print(index)
    return index
    
def rightStation(instance):
    global index
    global Images
    global MusicNameLabel
    layout.remove_widget(Images[index])
    layout.remove_widget(StationLabelNames[index])
    layout.remove_widget(MusicNameLabel)
    
    index = index + 1
    if index > len(Images)-1:
        index = 0
    
    check_switch()
    layout.add_widget(Images[index])
    layout.add_widget(StationLabelNames[index])
    
    if stationList[index].current_track in stationList[index].music_list:
        MusicName = stationList[index].current_music_track.upper()
        MusicName = MusicName.replace("_", " ")
        MusicNameLabel = Label(text=MusicName, pos=(0,-150), font_size = '30sp', bold = True, font_name = "CL1960")
        layout.add_widget(MusicNameLabel)
    
    print(index)
    return index

def MusicLabelUpdater(dt):
    global index
    global MusicNameLabel
    if stationList[index].current_track in stationList[index].music_list:
        layout.remove_widget(MusicNameLabel)
        MusicName = stationList[index].current_music_track.upper()
        MusicName = MusicName.replace("_"," ")
        MusicNameLabel = Label(text=MusicName, pos=(0,-150), font_size = '30sp', bold = True, font_name = "CL1960")
        layout.add_widget(MusicNameLabel)
    else:
        layout.remove_widget(MusicNameLabel)
    pass

class RadioWidget(App):
    def build(self):
        global layout
        global p1
        global p2
        global p3
        global p4
        global p5
        layout = FloatLayout() #background_color=(0.22,0.35,0.64,1))
        
        p1 = Thread(target=radio_mirror_park.playOneRadioCycle_infinite)
        p2 = Thread(target=non_stop_pop.playOneRadioCycle_infinite)
        p3 = Thread(target=los_santos_rock.playOneRadioCycle_infinite)
        p4 = Thread(target=rebel_radio.playOneRadioCycle_infinite)
        p5 = Thread(target=radio_los_santos.playOneRadioCycle_infinite)
        p1.start()
        p2.start()
        p3.start()
        p4.start()
        p5.start()

        
        button1 = Button (text="", pos=(117,165),
                          #background_color=(155/255,214/255,227/255,1),
                          size_hint=(0.18,0.18), background_normal='LeftArrow.png',
                          background_down='LeftArrowDown.png', border=(0,0,0,0))
        button1.bind(on_press=leftStation)
        
        button2 = Button (text="", pos=(667,165),
                          #background_color=(155/255,214/255,227/255,1),
                          size_hint=(0.18,0.18), background_normal='RightArrow.png',
                          background_down='RightArrowDown.png', border=(0,0,0,0))
        button2.bind(on_press=rightStation)
        
        
        layout.add_widget(button1)
        layout.add_widget(button2)
        
        Clock.schedule_interval(MusicLabelUpdater, 1)
        
        return layout

#====================================
#Main loop that runs the app

if __name__ == '__main__':

    RadioWidget().run()
