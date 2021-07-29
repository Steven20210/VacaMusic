from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def introduction():
    intro_paragraph = """
    Hi! Welcome to VacaMusic!
    
    Here, we will curate a list of artists based off of where you are in the world, so that you can 
    listen to local music that will enhance your vacation experience!!
    """
    print(intro_paragraph)
    locations = ['Country', "Province", "City"]
    location_responses = []

    for i in range(len(locations)):
        if i == (len(locations) - 1):
            place = input(locations[i] + ": ")
            location_responses.append(place)
        else:
            place = input(locations[i] + ": ")
            location_responses.append(place + ', ')

    return location_responses


# Create Google Chrome Instance:
def search_for_music(loc_responses):
    driver = webdriver.Chrome(r'C:\Users\Steven\Downloads\chromedriver_win32 (1)\chromedriver.exe')
    driver.implicitly_wait(10)
    driver.get('https://www.google.com/')
    search_field = driver.find_element_by_name('q')
    search_field.send_keys('all music ' + loc_responses[0] + loc_responses[1] + loc_responses[2])
    search_field.send_keys(Keys.ENTER)
    try:
        allmusic_element = driver.find_element_by_id('search')
        first_link = allmusic_element.find_element_by_tag_name('a')
        first_link.click()

        artist_links = driver.find_elements_by_class_name('birth_death_date_location')
        all_artists = artist_links[0].text
        split_all_artists = all_artists.split('\n')

        driver.close()

        return split_all_artists

    except:
        print("Your search result cannot be found")


def play_music(all_artist_list):
    for artist in all_artist_list[:10]:
        print(artist)

    user_input = input("Please input the name of the artist that you would like to listen to:")

    driver = webdriver.Chrome(r'C:\Users\Steven\Downloads\chromedriver_win32 (1)\chromedriver.exe')
    driver.implicitly_wait(10)
    driver.get('https://www.youtube.com/')
    search_field = driver.find_element_by_xpath('//*[@id="search"]')
    search_field.send_keys(user_input)
    time.sleep(3)
    search_field.send_keys(Keys.ENTER)


    try:
        # Click on the music video
        allmusic_element = driver.find_element_by_xpath('//*[@id="contents"]/ytd-video-renderer[1]')
        first_link = allmusic_element.find_element_by_tag_name('a')
        first_link.click()

        stop = False

        while not stop:
            time.sleep(10)
            user_wait = input("Do you want to stop playing the music: (type in y or n)")
            if user_wait == 'y':
                stop = True
                driver.close()

    except:
        print("Your search result cannot be found")


def run():
    loc_responses = introduction()
    artist_list = search_for_music(loc_responses)
    play_music(artist_list)


run()
