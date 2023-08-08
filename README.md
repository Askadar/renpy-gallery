# Renpy Gallery module

WIP thing to allow customizable and functional gallery in renpy projects

## How to

**Don't, it's not ready yet.**

Otherwise add the driver.rpy somewhere in your project, initialize global images list like
```renpy
define images = [
    ZNGalleryImage("bg club.jpg", seenImage="bg club", fullsize="bg club.jpg"),
    # ZNGalleryImage(thumbnail, seenImage=future trigger, rpy image string, fullsize=path to image inside images folder),
]
```

and then show gallery button anywhere you want with `show screen zn_gallery_button`.

But again, don't it's early wip and things should change.
