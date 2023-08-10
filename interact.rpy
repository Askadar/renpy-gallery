style zng_interact is hbox:
    xalign 0.0
    yalign 0.0

screen zn_gallery_button(text = "Open gallery"):
    hbox:
        style 'zng_interact'
        style_prefix 'zng_interact'

        textbutton text action ShowMenu('zn_gallery')
