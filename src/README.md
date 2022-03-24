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

## Using Geojson.io

In this section, I will delve into [Geojson.io](http://geojson.io/#map=2/20.0/0.0) and just provide a basic example of what I did throughout the map. Throughout the development process, I had to place a marker in a specific location of the map but also outline certain sections of the map, the question some would ask is how did I do that. Demonstrated below is how I was able to do it through geojson.io.

### Creating outline with Geojson.io

In this little section, I will demonstrate how I made a GEOJSON file for the Telecom Hall. Thanks to [geojson.io](http://geojson.io/#map=2/20.0/0.0) I was able to make the outline by manually creating lines over what I deem to be the correct outline for the telecom hall. Once I manually created the lines, it would look like the following on the website:

![telecommoutline](https://user-images.githubusercontent.com/49813790/159933780-c1db9487-1374-429e-b39c-8e6dfa785480.png)

Now the question is how does this image become added to the map in my program. Well, you see on [geojson.io](http://geojson.io/#map=2/20.0/0.0) once I completed that outline it has the following code displayed:

```
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "properties": {},
      "geometry": {
        "type": "LineString",
        "coordinates": [
          [
            -76.85033619403839,
            39.045863548505245
          ],
          [
            -76.8500954657793,
            39.04587240174798
          ],
          [
            -76.85009814798832,
            39.04591823028087
          ],
          [
            -76.85004316270351,
            39.04591979261668
          ],
          [
            -76.85005724430083,
            39.04613956084498
          ],
          [
            -76.85010753571986,
            39.046136436183026
          ],
          [
            -76.85011088848114,
            39.0461848684279
          ],
          [
            -76.85033217072487,
            39.04617809833114
          ],
          [
            -76.85033082962036,
            39.04613070763574
          ],
          [
            -76.85035161674023,
            39.04612914530458
          ],
          [
            -76.8503375351429,
            39.04586667317928
          ]
        ]
      }
    }
  ]
}
```

When we download the outline as a GEOJSON file, in my program I am able to do the following to display that outline on the Telecom hall on the created map:

```
 # Here we create an outline for the Telecom Hall and display it
    tele_cap = 'lab.geojson'
    display((folium.GeoJson(tele_cap, name="TeleComm").add_to(map_cap)))
```

Now that we have done this, when we run the program, the map will now have the Telecom hall outline as displayed below:

![telecomonmap](https://user-images.githubusercontent.com/49813790/159935295-c9b0e9f9-77ee-4703-a462-cd862bff0bdb.png)






### Creating pathway on geojson.io

Now that I was able to create the outline, I would need to manually create a pathway. Just like creating the outline, I would have to manually do this through the website. In this section, I will display a simple example of a pathway, let's say I want to display a pathway of going from the innovator's hall to McGowan. To do that I would first manually do that and get the following result:

![pathexample](https://user-images.githubusercontent.com/49813790/159936692-79c70b91-39ab-46f6-9544-5e76f365ac20.png)

We would then just copy the coordinates, inverse the order since it should be latitude first and then longitude instead of how we have it currently.

As displayed earlier before, we would then be given code that looks like the following given by [geojson.io](http://geojson.io/#map=2/20.0/0.0):

```
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "properties": {},
      "geometry": {
        "type": "LineString",
        "coordinates": [
          [
            -76.85196161270142,
            39.04526933714771
          ],
          [
            -76.85175508260727,
            39.045450569537614
          ],
          [
            -76.85161024332047,
            39.04538807566259
          ],
          [
            -76.85143858194351,
            39.04537974314173
          ],
          [
            -76.85083240270615,
            39.045400574442006
          ],
          [
            -76.85043007135391,
            39.045417239477814
          ],
          [
            -76.85044884681702,
            39.04584427967899
          ],
          [
            -76.85040324926376,
            39.04585052902862
          ],
          [
            -76.85045957565306,
            39.04698373528856
          ],
          [
            -76.85061782598495,
            39.04697748603918
          ],
          [
            -76.8510228395462,
            39.04750658719482
          ],
          [
            -76.85063123703003,
            39.04742118137102
          ],
          [
            -76.85065805912018,
            39.047716976710525
          ],
          [
            -76.8507519364357,
            39.04775030568522
          ],
          [
            -76.85080826282501,
            39.04782737887897
          ],
          [
            -76.85091823339462,
            39.0478669569728
          ],
          [
            -76.8509128689766,
            39.04794403003922
          ],
          [
            -76.85093432664871,
            39.047966943637384
          ]
        ]
      }
    }
  ]
}
```

as displayed below, we used the path we created prior to this example which is the walking and jogging path, and have the following code to have the path visualized on the map:

```
# This creates the pathway for the route I believe is the best route for students and visitors to go thrpugh to enjoy a nice scenic but also quiet walk/jog
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

which would provide us with the pathway displayed in the final map which is displayed in the following section.



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




