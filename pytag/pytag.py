#!/usr/bin/env python
# -*- coding: utf-8 -*- 
'''
Created on 28 Jul 2016

@author: af
'''

from pytagcloud import create_tag_image, make_tags
import re
from pytagcloud.lang.stopwords import StopWords
from operator import itemgetter
from wordcloud import WordCloud, get_single_color_func

def get_tag_counts(text):
    """
    Search tags in a given text. The language detection is based on stop lists.
    This implementation is inspired by https://github.com/jdf/cue.language. Thanks Jonathan Feinberg.
    """
    words = map(lambda x:x.lower(), re.findall(r'[@#]*\w+', text, re.UNICODE))
    
    s = StopWords()     
    s.load_language(s.guess(words))
    
    counted = {}
    
    for word in words:
        if not s.is_stop_word(word) and len(word) > 1:
            if counted.has_key(word):
                counted[word] += 1
            else: 
                counted[word] = 1
      
    return sorted(counted.iteritems(), key=itemgetter(1), reverse=True)
YOUR_TEXT = " berlin berlin berlin berlin berlin berlin berlin berlin berlin berlin berlin berlin berlin berlin berlin berlin berlin berlin berlin berlin berlin berlin berlin berlin berlin berlin berlin berlin berlin berlin #berlin #berlin #berlin #berlin #berlin #berlin #berlin #berlin #berlin #berlin #berlin #berlin #berlin #berlin #berlin #berlin #berlin #berlin #berlin #berlin #berlin #berlin #berlin #berlin #berlin #berlin #berlin #berlin #berlinale #berlinale #berlinale #berlinale #berlinale #berlinale #berlinale #berlinale #berlinale #berlinale #berlinale #berlinale #berlinale #berlinale #berlinale #berlinale #berlinale #berlinale berliner berliner berliner berliner berliner berliner berliner berliner berliner berliner berliner berliner berliner berliner berliner berliner berliner alexanderplatz alexanderplatz alexanderplatz alexanderplatz alexanderplatz alexanderplatz alexanderplatz alexanderplatz alexanderplatz alexanderplatz alexanderplatz alexanderplatz alexanderplatz bhf bhf bhf bhf bhf bhf bhf bhf bhf bhf bhf bhf #extremecrm #extremecrm #extremecrm #extremecrm #extremecrm #extremecrm #extremecrm #extremecrm #extremecrm #extremecrm #extremecrm #extremecrm german german german german german german german german german german german friedrichshain friedrichshain friedrichshain friedrichshain friedrichshain friedrichshain friedrichshain friedrichshain friedrichshain friedrichshain friedrichshain neukölln neukölln neukölln neukölln neukölln neukölln neukölln neukölln neukölln neukölln neukölln brandenburger brandenburger brandenburger brandenburger brandenburger brandenburger brandenburger brandenburger brandenburger brandenburger brandenburger berlinale berlinale berlinale berlinale berlinale berlinale berlinale berlinale berlinale berlinale berlinale oberholz oberholz oberholz oberholz oberholz oberholz oberholz oberholz oberholz oberholz #28c3 #28c3 #28c3 #28c3 #28c3 #28c3 #28c3 #28c3 #28c3 #28c3 chemnitz chemnitz chemnitz chemnitz chemnitz chemnitz chemnitz chemnitz chemnitz chemnitz budapester budapester budapester budapester budapester budapester budapester budapester budapester budapester der der der der der der der der der der schickes schickes schickes schickes schickes schickes schickes schickes schickes berghain berghain berghain berghain berghain berghain berghain berghain berghain kreuzberg kreuzberg kreuzberg kreuzberg kreuzberg kreuzberg kreuzberg kreuzberg kreuzberg charlottenburg charlottenburg charlottenburg charlottenburg charlottenburg charlottenburg charlottenburg charlottenburg charlottenburg #teatimebln #teatimebln #teatimebln #teatimebln #teatimebln #teatimebln #teatimebln #teatimebln #teatimebln #sbahn #sbahn #sbahn #sbahn #sbahn #sbahn #sbahn #sbahn herzen herzen herzen herzen herzen herzen herzen herzen #wulff #wulff #wulff #wulff #wulff #wulff #wulff #wulff curser curser curser curser curser curser curser curser hostel hostel hostel hostel hostel hostel hostel hostel potsdam potsdam potsdam potsdam potsdam potsdam potsdam potsdam mitte mitte mitte mitte mitte mitte mitte mitte readmill readmill readmill readmill readmill readmill readmill readmill bäckerei bäckerei bäckerei bäckerei bäckerei bäckerei bäckerei bäckerei #diablo3 #diablo3 #diablo3 #diablo3 #diablo3 #diablo3 #diablo3 bvg bvg bvg bvg bvg bvg bvg mit mit mit mit mit mit mit ys ys ys ys ys ys ys platz platz platz platz platz platz platz freddy freddy freddy freddy freddy freddy freddy rosenthaler rosenthaler rosenthaler rosenthaler rosenthaler rosenthaler rosenthaler potsdamer potsdamer potsdamer potsdamer potsdamer potsdamer potsdamer chilton chilton chilton chilton chilton chilton chilton náměstí náměstí náměstí náměstí náměstí náměstí náměstí mensch mensch mensch mensch mensch mensch mensch onions onions onions onions onions onions onions homesick homesick homesick homesick homesick homesick homesick berliners berliners berliners berliners berliners berliners berliners angelis angelis angelis angelis angelis angelis angelis str str str str str str str nickleback nickleback nickleback nickleback nickleback nickleback nickleback mmt mmt mmt mmt mmt mmt mmt nen nen nen nen nen nen nen keule keule keule keule keule keule #blogrefresh #blogrefresh #blogrefresh #blogrefresh #blogrefresh #blogrefresh schönefeld schönefeld schönefeld schönefeld schönefeld schönefeld #smwberlin #smwberlin #smwberlin #smwberlin #smwberlin #smwberlin txl txl txl txl txl txl überall überall überall überall überall überall 30b 30b 30b 30b 30b 30b berlín berlín berlín berlín berlín berlín betahaus betahaus betahaus betahaus betahaus betahaus germany germany germany germany germany germany urlaub urlaub urlaub urlaub urlaub urlaub jeht jeht jeht jeht jeht jeht bayer bayer bayer bayer bayer bayer viper viper viper viper viper viper #voice #voice #voice #voice #voice #voice laune laune laune laune laune laune niemand niemand niemand niemand niemand niemand ich ich ich ich ich ich crisis crisis crisis crisis crisis crisis #gddde #gddde #gddde #gddde #gddde #gddde railroads railroads railroads railroads railroads railroads café café café café café café tegel tegel tegel tegel tegel tegel #goldenglobes #goldenglobes #goldenglobes #goldenglobes #goldenglobes #goldenglobes nich nich nich nich nich nich fernsehturm fernsehturm fernsehturm fernsehturm fernsehturm fernsehturm heut heut heut heut heut hacking hacking hacking hacking hacking youtub youtub youtub youtub youtub cisse cisse cisse cisse cisse prenzlauer prenzlauer prenzlauer prenzlauer prenzlauer feedback feedback feedback feedback feedback pure pure pure pure pure jetlagging jetlagging jetlagging jetlagging jetlagging jak jak jak jak jak und und und und und steglitz steglitz steglitz steglitz steglitz allee allee allee allee allee espresso espresso espresso espresso espresso borrow borrow borrow borrow borrow #tm2k12 #tm2k12 #tm2k12 #tm2k12 #tm2k12 #artist #artist #artist #artist #artist forklifted forklifted forklifted forklifted forklifted ick ick ick ick ick arrived arrived arrived arrived arrived wort wort wort wort wort pfeift pfeift pfeift pfeift pfeift cancelled cancelled cancelled cancelled cancelled hallo hallo hallo hallo hallo roule roule roule roule roule poland poland poland poland poland hug hug hug hug hug #hp #hp #hp #hp #hp wunderlist wunderlist wunderlist wunderlist wunderlist #chemnitz #chemnitz #chemnitz #chemnitz #chemnitz ut ut ut ut ut chat chat chat chat chat sozialen sozialen sozialen sozialen sozialen tor tor tor tor tor mulino mulino mulino mulino mulino wahrheit wahrheit wahrheit wahrheit wahrheit #linkeddata #linkeddata #linkeddata #linkeddata #linkeddata verkauf verkauf verkauf verkauf verkauf ostbahnhof ostbahnhof ostbahnhof ostbahnhof ostbahnhof zentrum zentrum zentrum zentrum zentrum urania urania urania urania urania von von von von von deutscher deutscher deutscher deutscher deutscher javascript javascript javascript javascript javascript #germany #germany #germany #germany ringbahn ringbahn ringbahn ringbahn illustrations illustrations illustrations illustrations spain spain spain spain olympiastadion olympiastadion olympiastadion olympiastadion lazy lazy lazy lazy studio studio studio studio yedili yedili yedili yedili costs costs costs costs language language language language wooo wooo wooo wooo hertha hertha hertha hertha useful useful useful useful arrive arrive arrive arrive awesomeness awesomeness awesomeness awesomeness ruby ruby ruby ruby release release release release zemřel zemřel zemřel zemřel #potsdam #potsdam #potsdam #potsdam praha praha praha praha starts starts starts starts #getamen #getamen #getamen #getamen parameters parameters parameters parameters soundcloud soundcloud soundcloud soundcloud hosbulduk hosbulduk hosbulduk hosbulduk besten besten besten besten #startups #startups #startups #startups internet internet internet internet das das das das nomad nomad nomad nomad ebay ebay ebay ebay #robotics #robotics #robotics #robotics leipzig leipzig leipzig leipzig kottbusser kottbusser kottbusser kottbusser gloom gloom gloom gloom germans germans germans germans freitag freitag freitag freitag totally totally totally totally europe europe europe europe haste haste haste haste jb jb jb jb kann kann kann kann lots lots lots lots telefon telefon telefon telefon damm damm damm damm что что что что mooorning mooorning mooorning mooorning hackescher hackescher hackescher hackescher patterns patterns patterns patterns friedrichstraße friedrichstraße friedrichstraße friedrichstraße очень очень очень очень gesellschaft gesellschaft gesellschaft gesellschaft crawl crawl crawl crawl thine thine thine thine של של של של woodkid woodkid woodkid woodkid blergh blergh blergh blergh transmediale transmediale transmediale transmediale vor vor vor vor inhale inhale inhale inhale schatzi schatzi schatzi schatzi dj dj dj dj en en en en bahn bahn bahn bahn disco disco disco disco umgeben umgeben umgeben umgeben shutdown shutdown shutdown shutdown nr nr nr nr alexa alexa alexa alexa bastards bastards bastards model model model foster foster foster dossi dossi dossi glueck glueck glueck #internetradio #internetradio #internetradio gleich gleich gleich pis pis pis #bvg #bvg #bvg zu zu zu wirf wirf wirf tadaa tadaa tadaa"

#pytagcloud
#tags = make_tags(get_tag_counts(YOUR_TEXT), maxsize=120)
#create_tag_image(tags, 'cloud_large.png', size=(1800, 1200), fontname='PT Sans Regular')




text = YOUR_TEXT

# Generate a word cloud image
wordcloud = WordCloud(max_words=300, mode='RGBA', background_color=None, width=1200, height=600, max_font_size=100, relative_scaling=.5).generate(text)

# Display the generated image:
# the matplotlib way:
import matplotlib.pyplot as plt
plt.imshow(wordcloud)
plt.axis("off")
plt.show()

# take relative word frequencies into account, lower max_font_size
#color_func=get_single_color_func('darkred')
#wordcloud = WordCloud(max_words=300, mode='RGBA', background_color=None, width=500, height=300, max_font_size=50, relative_scaling=.5).generate(text)
#plt.figure()
#plt.imshow(wordcloud)
#plt.axis("off")
#plt.show()
