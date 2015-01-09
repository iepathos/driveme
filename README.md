# Drive Me

Uses Google Maps to automatically drive you through the street view of a specified route.

## Rough Project Outline
- user enters route directions, from and to
- [DirectionsRoutes.overview_path](https://developers.google.com/maps/documentation/javascript/directions) will provide us with the array of coordinates along route
- compile list of streetview map links to list of latitude and longitude coordinates
- add timer to progress through list of image links
- add pause and play
- add rewind, fast forward and speed control faster and slower