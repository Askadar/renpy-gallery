default images = zngImages
default filteredImages = images

default tag = "all"
default char = "all"

style zng is frame:
    background Solid('#414141')
    xalign 0.5
    yalign 0.5
    padding (0, 0)

style zng_thumbnail_frame is frame:
    background Solid('#00000080')
    padding (12, 12)
    yalign 1.0

style zng_thumbnail_locked is frame:
    background Solid('#00000080')
    padding (0, 0)
    yalign 0.5

style zng_thumbnail_text is text:
    xalign 0.5
    yalign 0.5
    size 36

style zng_wrap is vbox:
    xalign 0.5
    yalign 0.5

style zng_vpgrid is vpgrid:
    margin (0, 0)

style zng_menu_main is hbox:
    xalign 0.5

style zng_menu_title is text:
    size 64

style zng_menu_action is hbox:
    xalign 1.0
    yalign 0.0
    ysize 76

style zng_menu_action_button is button:
    yalign 0.5

style zng_menu_button is button:
    yalign 0.5

style zng_menu_hbox is hbox:
    spacing 64

style zng_menu_hbox_sub is hbox:
    spacing 16
    yalign 0.5

screen zn_gallery(thumbnailWidth = 480, aspectRatio = 1.78, gridSpacing = (16, 16), thumbnailPadding = (0, 0), backButtonText = "Close"):
    default screenSize = (config.screen_width, config.screen_height)
    default columnCount = 3
    default rowCount = 3
    default thumbnailSize = (thumbnailWidth, int(thumbnailWidth / aspectRatio))
    default paddedThumbnailSize = (thumbnailSize[0] - (thumbnailPadding[0] * 2), thumbnailSize[1] - (thumbnailPadding[1] * 2))
    default frameHeight = screenSize[1]

    $ columnCount = int(screenSize[0] / (thumbnailSize[0] + gridSpacing[0]))
    $ rowCount = int(screenSize[1] / (thumbnailSize[1] + gridSpacing[1]))

    $ filteredImages = images if tag == "all" and char == "all" else filter(lambda i: char in i.chars, images) if char != "all" else filter(lambda i: tag in i.tags, images) if tag != "all" else filter(lambda i: char in i.chars and tag in i.tags, images)

    modal True

    zorder 5
    frame:
        style 'zng'
        style_prefix 'zng'

        xysize screenSize

        hbox:
            style 'zng_menu_main'
            style_prefix 'zng_menu'

            hbox:
                text "Gallery":
                    style 'zng_menu_title'
                hbox:
                    style 'zng_menu_hbox_sub'
                    textbutton "Tag: {}".format(zngTags[tag] if tag != "all" else "All Tags") action Show('zng_select', dict=zngTags, var="tag")
                    textbutton "Character: {}".format(zngCharacters[char] if char != "all" else "All Characters") action Show('zng_select', dict=zngCharacters, var="char")

        hbox:
            style 'zng_menu_action'
            style_prefix 'zng_menu_action'
            textbutton backButtonText keysym "game_menu" action Hide("zn_gallery")

        vbox:
            style 'zng_wrap'

            vpgrid:
                draggable True
                mousewheel True

                if len(images) > columnCount * rowCount:
                    scrollbars 'vertical'

                cols columnCount
                spacing gridSpacing[0]
                yspacing gridSpacing[1]

                for i in filteredImages:
                    frame:
                        style_prefix 'zng_thumbnail'
                        padding thumbnailPadding
                        xysize thumbnailSize
                        imagebutton:
                            idle Transform(i.thumbnail, matrixcolor = TintMatrix('#fff'), xysize = paddedThumbnailSize)
                            hover Transform(i.thumbnail, matrixcolor = TintMatrix('#a6eaff'), xysize = paddedThumbnailSize)
                            insensitive Transform(i.thumbnail, matrixcolor = TintMatrix('#777'), xysize = paddedThumbnailSize)
                            action i.action
                            sensitive persistent.zng_unlocked or (i.isImageUnlocked()) or (i.isSceneUnlocked())

                        if persistent.zng_unlocked or (i.isImageUnlocked()) or (i.isSceneUnlocked()):
                            frame:
                                xsize thumbnailSize[0]
                                text i.title
                        else:
                            frame:
                                style 'zng_thumbnail_locked'
                                xsize thumbnailSize[0]
                                ysize thumbnailSize[1]
                                text "Locked"


style zng_select_viewport is viewport:
    xfill False
    yfill False

style zng_select_inner_viewport is viewport:
    xfill False
    yfill False

style zng_select_vbox is vbox:
    spacing 24

style zng_select_inner_vbox is vbox:
    spacing 16

screen zng_select(dict = zngTags, var = "tag"):
    modal True
    style_prefix 'zng_select'

    zorder 10
    frame:
        background Frame(Solid('#262626'), gui.notify_frame_borders, tile=gui.frame_tile)
        pos(renpy.get_mouse_pos()[0], renpy.get_mouse_pos()[1])
        padding (16, 16)

        vbox:
            viewport:
                style_prefix 'zng_select_inner'
                vbox:
                    textbutton "All" action [SetVariable(var, "all"), Hide("zng_select")]

                    for i in dict:
                        textbutton dict[i] action [SetVariable(var, i), Hide("zng_select")]

            textbutton "Cancel" keysym "game_menu" action Hide("zng_select")
