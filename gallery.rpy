style zng is frame:
    background Solid('#777')
    xalign 0.5
    yalign 0.5
    padding (0, 0)

style zng_vbox is vbox:
    xalign 0.5
    yalign 0.5

style zng_vpgrid is vpgrid:
    margin (24, 24)

style zng_action is hbox:
    xalign 0.0

style zng_action_button_text is button_text:
    idle_color '#fff'
    hover_color '#ccc'

screen zn_gallery(images = zngImages, thumbnailWidth = 480, aspectRatio = 1.78, gridSpacing = (12, 24), thumbnailPadding = (4, 4), backButtonText = "Close"):
    default screenSize = (config.screen_width, config.screen_height)
    default columnCount = 3
    default rowCount = 3
    default thumbnailSize = (thumbnailWidth, int(thumbnailWidth / aspectRatio))
    default paddedThumbnailSize = (thumbnailSize[0] - (thumbnailPadding[0] * 2), thumbnailSize[1] - (thumbnailPadding[1] * 2))
    default frameHeight = screenSize[1]

    $ columnCount = int(screenSize[0] / (thumbnailSize[0] + gridSpacing[0]))
    $ rowCount = int(screenSize[1] / (thumbnailSize[1] + gridSpacing[1]))

    zorder 5
    frame:
        style 'zng'
        style_prefix 'zng'

        xysize screenSize

        hbox:
            style 'zng_action'
            style_prefix 'zng_action'
            textbutton backButtonText action Return(1)

        vbox:

            vpgrid:
                draggable True
                mousewheel True

                if len(images) > columnCount * rowCount:
                    scrollbars 'vertical'

                cols columnCount
                spacing gridSpacing[0]
                yspacing gridSpacing[1]

                for i in images:
                    frame:
                        padding thumbnailPadding
                        xysize thumbnailSize
                        imagebutton:
                            idle Transform(i.thumbnail, matrixcolor = TintMatrix('#fff'), xysize = paddedThumbnailSize)
                            hover Transform(i.thumbnail, matrixcolor = TintMatrix('#a6eaff'), xysize = paddedThumbnailSize)
                            insensitive Transform(i.thumbnail, matrixcolor = TintMatrix('#777'), xysize = paddedThumbnailSize)
                            action i.action
                            sensitive persistent.zng_unlocked or (i.seenImage is not None and renpy.seen_image(i.seenImage)) or (i.seenLabel is not None and renpy.seen_label(i.seenLabel))
