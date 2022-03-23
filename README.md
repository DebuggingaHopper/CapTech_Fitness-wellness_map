# CapTech_Fitness-wellness_map
This project is my submission for Capitol Tech Hackathon 2022, this is an interactive map of the university which contains events, and activities held on campus to help students fitness and mental wellness.

## Purpose

The purpose of this application is to follow the theme, which is to endorse fitness and mental wellness. Now the question is how can I do that with this application. I noticed that in Capitol Technology University, some students are not aware of the different activities that allow students to not only be physically fit but also be mentally well in their own way. To demonstrate this, I wanted to create an interactive map of the campus that includes the different activities and facilities I believe truly help students be physically fit but also be mentally well. I made this map under the idea of providing this to other students, so they are aware of these activities and facilities since from my experience they have helped me a lot to be mentally and physically well, and I believe this type of application not only fits my criteria for making one but also fits with the theme of endorsing fitness and mental wellness.


## Challanges

To be completely honest, there were some challenges I faced due to the fact I was initially lost when it came to what I wanted to create for this Hackathon. I was initially stumped, however after some time, I was able to figure out what I wanted to create. From there I faced the usual challenges like errors and little mix-ups I made visually that I then resolved later on in development. Overall I was able to make some good progress in the development of this application and ensuring the number of challenges was not as much as compared to previous projects.

## Resources utilized

Prior to making this project, I was essentially new to making an application that utilizes a map. I have never worked with maps nor really had to make an interactive map before. So while digging into the subject I found about the [Folium](https://python-visualization.github.io/folium/index.html) library which allowed me to create a basic map of the campus, and while playing around with it, I was able to do what I sought to do thanks to the [geojson.io](http://geojson.io/#map=2/20.0/0.0) also allowing the process to get the longitude and latitude values to become far easier.


### Final Map 

As you will see throughout the README file located in the src folder, by utilizing the Folium library and [Flask](https://flask.palletsprojects.com/en/2.0.x/), I was able to create the following output for my desired application: 

![Completed_Map](https://user-images.githubusercontent.com/49813790/159804636-f33afe57-15bf-48f7-bdb1-002f01eba539.png)

# Using Flask

Now that I have a good porition of the foundation completed, I want to be able for it to run on a [Flask](https://flask.palletsprojects.com/en/2.0.x/) Application. To do so, I had to do the following:

```
app = Flask(__name__)


@app.route('/')
def index():
    start_coords = (39.046900, -76.850400)
    map_cap = folium.Map(location=start_coords, width="100%", zoom_start=17)

    feild_cap = 'field.geojson'
    display(folium.GeoJson(feild_cap, name="Feild").add_to(map_cap))
....
....
....
....
....
....
return map_cap._repr_html_()


if __name__ == '__main__':
    app.run(debug=True)
```

This makes it so that the Map created is returned as an html and would have the app do the function index when executed displaying the user the created interactive map.






