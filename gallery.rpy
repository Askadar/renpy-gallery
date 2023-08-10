style zng is frame:
    zorder 5
    background Solid('#777')
    xalign 0.5
    yalign 0.3
    padding (0, 0)

style zng_vpgrid is vpgrid:
    margin (24, 24)

style zng_action is hbox:
    xalign 0.5
    margin (24, 0)

style zng_action_button_text is button_text:
    idle_color '#fff'
    hover_color '#ccc'

screen zn_gallery(columnCount = 4, rowCount = 3, images = zngImages):
    default twidth = 400
    default theight = 260
    default tpadding = 4
    default t2padding = tpadding * 2
    default spacing = 12
    default yspacing = 24

    frame:
        style 'zng'
        style_prefix 'zng'

        vbox:
            vpgrid:
                cols columnCount
                draggable True
                mousewheel True

                if len(images) > columnCount * rowCount:
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
                            hover Transform(i.thumbnail, matrixcolor=TintMatrix('#a6eaff'),xysize=(twidth-t2padding,theight-t2padding))
                            insensitive Transform(i.thumbnail, matrixcolor=TintMatrix('#777'),xysize=(twidth-t2padding,theight-t2padding))
                            action i.action
                            sensitive persistent.zng_unlocked or (i.seenImage is not None and renpy.seen_image(i.seenImage)) or (i.seenLabel is not None and renpy.seen_label(i.seenLabel))

                        text "sauce [i.thumbnail]"

            hbox:
                style 'zng_action'
                style_prefix 'zng_action'
                textbutton "Return" action Return(1)
