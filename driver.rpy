# HOPE on deez nuts
# Gallery + filters on char + filters on tags + compile of lists from constructors + (support mobile?)
# Gallery - screen + preview buttons
# Image? - screen + fullsize image
# Replay - scene call + return

# Filters - logic to store compiled lists\dicts and use them for sorting


init python:
    class ZNGalleryImage:
        def __init__(
            self, thumbnail,
            fullsize = None, label = None,
            seenImage = None, seenLabel = None

            ):
            if (fullsize is None and label is None) or (fullsize is not None and label is not None):
                raise ValueError("[ZNGalleryImage] You have to pass either `fullsize` image or `label` name. Either is used to open gallery replay. You can't pass both at the same time.")
            if (seenImage is None and seenLabel is None) or (seenImage is not None and seenLabel is not None):
                raise ValueError("[ZNGalleryImage] You have to pass either `seenImage` image or `seenLabel` name. Either is used to enable gallery entry for replay. You can't pass both at the same time.")

            self.fullsize = fullsize
            self.label = label
            self.thumbnail = thumbnail
            self.action = ShowTransient('zn_gallery_replay', None, fullsize) #if fullsize else Call(label)

screen zn_gallery_button(text = "Open gallery"):
    hbox:
        spacing 25
        textbutton text:
            action ShowMenu('zn_gallery')
            # xysize (200, 80)

style zng is frame:
    background Solid('#777')
    xalign 0.5
    yalign 0.3
    padding (0, 0)

style zng_vpgrid is vpgrid:
    margin (24, 24)

screen zn_gallery(columnCount = 4):
    default twidth = 400
    default theight = 260
    default tpadding = 4
    default t2padding = tpadding * 2
    default spacing = 12
    default yspacing = 24

    default rowCount = 3

    frame:
        style 'zng'
        style_prefix 'zng'

        vpgrid:
            cols columnCount
            draggable True
            mousewheel True

            if len(images) > 6:
                scrollbars 'vertical'

            ymaximum (theight * rowCount) + (yspacing * (rowCount + 1))
            yspacing yspacing
            xspacing spacing

            for i in images:
                frame:
                    xysize (twidth, theight)
                    padding (tpadding, tpadding)
                    imagebutton:
                        idle Transform(i.thumbnail, matrixcolor=TintMatrix('#fff'),xysize=(twidth-t2padding,theight-t2padding))
                        hover Transform(i.thumbnail, matrixcolor=TintMatrix('#fcfa92'),xysize=(twidth-t2padding,theight-t2padding))
                        action i.action

                    add Text ("sauce [i.thumbnail]")

screen zn_gallery_replay(source):
    frame:
        background Transform(source, xysize=(1920, 1080))
        padding (0,0)
        xysize (1920, 1080)
