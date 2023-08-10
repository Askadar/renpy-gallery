style zng_interact is hbox:
    spacing 25
    xalign 0.5
    yalign 0.5

style zng_interact_textbutton is textbutton:
    xysize (50, 300)

screen zn_gallery_button(text = "Open gallery"):
    hbox:
        style 'zng_interact'
        style_prefix 'zng_interact'

        textbutton text:
            action ShowMenu('zn_gallery')
