# The main Source File

Within here, you will have access to the main .py file. If you go to the next folder, you will have access to all the PNG files, and GEOJSON files utilized for this project.

## The necessary Library for making a basic map

So before anything, let's delve into the code of this program. I made this a flask application that essentially just shows the user an interactive map of the University. To Display said map, I had to use the [Folium](https://python-visualization.github.io/folium/index.html) library and write the following lines of code:

```
start_coords = (39.046900, -76.850400)
map_cap = folium.Map(location=start_coords, width="100%", zoom_start=17)
```

I was able to acquire the longitude and latitude thanks to Google maps providing said information, making it very easy to acquire this information prior to actually making the map. Then, if we just call the map in the Jupyter notebook, it would give us the following output:

![Default_map](https://user-images.githubusercontent.com/49813790/159801992-806c7e78-f039-444c-896e-05fa7e1cf59a.png)

What I wanted to accomplish was to make some changes on the map by highlighting certain locations and placing markers with specific icons that when touched upon display information about the activity or facility. To do so is very simple thanks to the folium library, which allows me to do the following with the following code:

```
feild_cap = 'field.geojson'
display(folium.GeoJson(feild_cap, name="Feild").add_to(map_cap))
location_feild = [39.046041133926806, -76.85143992304802]
    iconfeild = folium.features.CustomIcon('Net.png', icon_size=(25, 25))
    popupfeild = "This is the Capitol Technology Field where students can do sports and other activites on campus. Even on a small campus students can keep themselves physcially active through outdoor activities."
    folium.Marker(location=location_feild, popup=popupfeild, icon=iconfeild).add_to(map_cap)
```

You may be wondering how did I make this GeoJson file, and I want to thank [geojson.io](http://geojson.io/#map=2/20.0/0.0) which allowed me to make the GeoJson files of the specified locations very easily. Now thanks to that same website I was able to acquire specific latitude and longitude files to place the markers exactly where I want them to be located. I would then make sure that the icon is a custom icon, that the popup is what I want the user to know, and finally add it to the map we created previously.

## Creating a pathway for a jogging/walking route

We would then do this for various other locations and facilities which would finally leave us with the final part I wanted to implement which was a path users can see as an ideal walking/jogging path I believe is the best to ensure you not only have a good jog but also have enough time for yourself. I took into account the scenery one would see as a student, while also taking into account the total time this would take from my estimation. To make the path, I would then need to write the following line of code:

```
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
```

Once again, thanks to [geojson.io](http://geojson.io/#map=2/20.0/0.0)I was able to acquire all the necessary latitude and longitude values for the pathway I wanted to display. I also used the plugin known as AntPath to display this pathway with a nice effect as demonstrated below:

![Completed_Map](https://user-images.githubusercontent.com/49813790/159804636-f33afe57-15bf-48f7-bdb1-002f01eba539.png)




