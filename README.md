# Renpy Gallery module (Alpha)

WIP Gallery module (not using built-in Gallery class) that allows to easily set up gallery in your game or mod it in.

To start either initialize global entries list via:

```renpy
define zngImages = [
    ZNGalleryImage(thumbnail="image.jpg", seenImage="image", fullsize="image.jpg"),
    # Using images only
    # ZNGalleryImage(
    #    thumbnail=<full path with extension from images folder>,
    #    seenImage=<renpy image tag user has to see to unlock entry>,
    #    fullsize=<full path with extension to full size image>,
    # ),
    # Or to have entries jump to label (UNTESTED)
    # ZNGalleryImage(
    #    thumbnail=<full path with extension from images folder>,
    #    seenLabel=<label tag that user has to see to unlock entry>,
    #    label=<label tag to jump to>,
    # ),
    # You can combine unlock condition and entry type, e.g. unlock image when user has read label
    # ZNGalleryImage(
    #    thumbnail=<full path with extension from images folder>,
    #    seenLabel=<label tag that user has to see to unlock entry>,
    #    fullsize=<full path with extension to full size image>,
    # ),
]
```

And add button to open gallery either via basic top-left button in your *script* `show screen zn_gallery_button()` or by adding your own custom button somewhere in your *screen* `textbutton text action ShowMenu('zn_gallery')`.

There is some customization available for main gallery screen:
```renpy
zn_gallery(
    images = zngImages, # list of images to use for this gallery, default to globally defined images list
    thumbnailWidth = # thumbnail preview width,
    aspectRatio = 1.78, # aspect ratio width/height, 1.78 means normal 16:9 ratio
    gridSpacing = (12, 24), # space between thumbnail previews, (horizontal, vertical)
    thumbnailPadding = (4, 4), # thumbnail padding (in case you want to use custom border image)
    backButtonText = "Close", # text that shows on back button
)
```

As well as styling customization via `zng` and `zng_interact` prefixes for gallery and interact screen respectively.
