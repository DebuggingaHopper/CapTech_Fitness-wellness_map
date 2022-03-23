from IPython.core.display import display
from flask import Flask

import folium
from folium import plugins

app = Flask(__name__)


@app.route('/')
def index():
    start_coords = (39.046900, -76.850400)
    map_cap = folium.Map(location=start_coords, width="100%", zoom_start=17)

    feild_cap = 'field.geojson'
    display(folium.GeoJson(feild_cap, name="Feild").add_to(map_cap))

    basketball_cap = 'basketball.geojson'
    display((folium.GeoJson(basketball_cap, name="BasketBall").add_to(map_cap)))

    mcgowan_cap = 'McGowan.geojson'
    display((folium.GeoJson(mcgowan_cap, name="McGowan").add_to(map_cap)))

    ComHall_cap = 'MA.geojson'
    display((folium.GeoJson(ComHall_cap, name="Megabyte").add_to(map_cap)))

    pond_cap = 'Pond.geojson'
    display((folium.GeoJson(pond_cap, name="CapitolPond").add_to(map_cap)))

    tele_cap = 'lab.geojson'
    display((folium.GeoJson(tele_cap, name="TeleComm").add_to(map_cap)))

    library_cap = 'library.geojson'
    display((folium.GeoJson(library_cap, name="Library").add_to(map_cap)))

    aud_cap = 'Auditorium.geojson'
    display((folium.GeoJson(aud_cap, name="Auditorium").add_to(map_cap)))

    innovators_cap = 'innovators.geojson'
    display((folium.GeoJson(innovators_cap, name="Innovators").add_to(map_cap)))

    location_feild = [39.046041133926806, -76.85143992304802]
    iconfeild = folium.features.CustomIcon('Net.png', icon_size=(25, 25))
    popupfeild = "This is the Capitol Technology Field where students can do sports and other activites on campus. Even on a small campus students can keep themselves physcially active through outdoor activities."
    folium.Marker(location=location_feild, popup=popupfeild, icon=iconfeild).add_to(map_cap)

    location_cf = [39.04522194584261, -76.85134805738926]
    iconcf = folium.features.CustomIcon('campfire.png', icon_size=(25, 25))
    popupcf = "Not known to many but there are various camp fire events held that allow students to communicate and be able to relieve stress by just relaxing near the fire."
    folium.Marker(location=location_cf, popup=popupcf, icon=iconcf).add_to(map_cap)

    location_ma = [39.04526100461285, -76.85116767883301]
    iconma = folium.features.CustomIcon('guitar.png', icon_size=(25, 25))
    popupma = "Occasioanlyl students play their instruments allowing many to be able to enjoy soothing and humorous music to ease their minds."
    folium.Marker(location=location_ma, popup=popupma, icon=iconma).add_to(map_cap)

    location_bc = [39.047897682056664, -76.85303248465061]
    iconbc = folium.features.CustomIcon('Basketball.png', icon_size=(10, 10))
    popupbc = "The University has a basketball which requires a little walk which makes it an excellent spot for students to not only do a jog but also have a game of basketball making sure they have alone time while also going all out on the court."
    folium.Marker(location=location_bc, popup=popupbc, icon=iconbc).add_to(map_cap)

    location_mc = [39.04807213778794, -76.85123473405838]
    iconmc = folium.features.CustomIcon('cyberlab.png', icon_size=(25, 25))
    popupmc = "To ensure students can focus, the Cyber Battle Lab allows students to be able to relax while learning more about cyber security."
    folium.Marker(location=location_mc, popup=popupmc, icon=iconmc).add_to(map_cap)

    folium.Marker(location=[39.04716496327999, -76.85037106275558],
                  popup='Here students can relax and converse with their fellow students while enjoying a nice meal or coffee to ease their minds',
                  icon=folium.features.CustomIcon('cofee.png', icon_size=(14, 14))).add_to(map_cap)

    folium.Marker(location=[39.04711288631855, -76.85021013021469],
                  popup='Students tend to play fighting games to ease their minds, and is an ideal spot to let loose',
                  icon=folium.features.CustomIcon('VS.png', icon_size=(14, 14))).add_to(map_cap)

    folium.Marker(location=[39.047081640123295, -76.85111202299595],
                  popup='one tends to forget that the best things to better mental helath is embracing nature. Here you can see the wildlife and enjoy a nice view',
                  icon=folium.features.CustomIcon('turtle.png', icon_size=(14, 14))).add_to(map_cap)
    folium.Marker(location=[39.04609529478764, -76.85011491179466],
                  popup='From 6PM -10PM, students can also relax in the Esports Lab so they can play some competitive games to allow them to relieve stressallowing students to keep a healthy mind.',
                  icon=folium.features.CustomIcon('Esports.png', icon_size=(20, 20))).add_to(map_cap)

    folium.Marker(location=[39.047289427062246, -76.85026545077562],
                  popup='One of our two pool table locations where students can enjoy a nice releaxing game of pool.',
                  icon=folium.features.CustomIcon('pool_table.png', icon_size=(14, 14))).add_to(map_cap)

    folium.Marker(location=[39.04673480642748, -76.8514533340931],
                  popup='Throughout the university, students tend to fly drones in different spots allowing those students to relax while enjoying their creations',
                  icon=folium.features.CustomIcon('Drone.png', icon_size=(18, 18))).add_to(map_cap)

    folium.Marker(location=[39.046890517261325, -76.85065202414988],
                  popup='Throughout the university, students tend to fly drones in different spots allowing those students to relax while enjoying their creations',
                  icon=folium.features.CustomIcon('Drone.png', icon_size=(18, 18))).add_to(map_cap)

    folium.Marker(location=[39.04537766001136, -76.85210645198822],
                  popup='One of our two pool table locations where students can enjoy a nice releaxing game of pool.',
                  icon=folium.features.CustomIcon('pool_table.png', icon_size=(14, 14))).add_to(map_cap)

    folium.Marker(location=[39.04671501706615, -76.8498332798481],
                  popup='The library allows students to relax while also being able to work peacefully and enjoy the silence and scenery.',
                  icon=folium.features.CustomIcon('library.png', icon_size=(14, 14))).add_to(map_cap)

    folium.Marker(location=[39.045762777693604,-76.85207158327101],
                  popup='Recently students have made a Casino Night where students can play black jack and poker without the risk of losing actual money but rather just enjoy themselves.',
                  icon=folium.features.CustomIcon('casino.png', icon_size=(14, 14))).add_to(map_cap)

    folium.Marker(location=[39.045293032788315,-76.85201056301594],
                  popup='The Adventure club allows students to participate in fun events such as the GoKart Event occuring on April 1st 2022',
                  icon=folium.features.CustomIcon('Adventure.png', icon_size=(14, 14))).add_to(map_cap)

    folium.Marker(
        location=[39.04539953287714,-76.85084715485573],
        popup='The following route is one students can take for a jog or walk to enjoy some time of tranquility.',
    ).add_to(map_cap)

    folium.Marker(
        location=[39.04582292773025,-76.85019940137862], # coordinates for the marker (Earth Lab at CU Boulder)
        popup='We have a tour on 3/25 and an open house on 3/26, this can help students who volunteer to be able to improve their communication skills while helping others.', # pop-up label for the marker,
        icon=folium.features.CustomIcon('Logo.png', icon_size=(14,14))
    ).add_to(map_cap)



    folium.plugins.AntPath([[39.0454068238309, -76.85056149959563], [39.04540265757169, -76.85084581375122],
                            [39.045148515296106, -76.85081899166107], [39.04511935136995, -76.85203135013579],
                            [39.0451985105701, -76.85209572315216], [39.04526100461285, -76.85218691825867],
                            [39.04599426391757, -76.852245926857], [39.046327561085334, -76.85223519802094],
                            [39.04665669049524, -76.85234785079956], [39.04676917741028, -76.85225665569305],
                            [39.04676501123142, -76.85220837593079], [39.04693165819354, -76.85220301151276],
                            [39.04690666117428, -76.85272872447968], [39.047685730782455, -76.85276627540588],
                            [39.048085677617735, -76.85262680053711], [39.04840646667184, -76.85234248638153],
                            [39.04865643115863, -76.85187578201294], [39.04846895787647, -76.85174703598022],
                            [39.04856061154326, -76.85114085674286], [39.04853144902581, -76.85085654258728],
                            [39.04846895787647, -76.85082972049713], [39.048427297079535, -76.8506795167923],
                            [39.04741493216034, -76.85064733028412], [39.0475024210595, -76.85100674629211],
                            [39.047752388745614, -76.85125887393951], [39.047885704483164, -76.85163974761963],
                            [39.04763990339632, -76.85172021389008], [39.047685730782455, -76.85196697711945],
                            [39.04738576916988, -76.85195624828339], [39.04739410145411, -76.8519937992096],
                            [39.047114969397754, -76.85198843479156], [39.047114969397754, -76.85202598571777],
                            [39.04692749202428, -76.85203135013579], [39.04698581837158, -76.85045421123505],
                            [39.04584427967899, -76.85040593147278], [39.04584427967899, -76.85045421123505],
                            [39.0454068238309, -76.8504273891449], [39.0454068238309, -76.8505346775055]]).add_to(
        map_cap)
    return map_cap._repr_html_()


if __name__ == '__main__':
    app.run(debug=True)
