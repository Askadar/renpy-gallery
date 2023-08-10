style zng_replay_image is frame:
    padding (0, 0)

style zng_replay_image_image_button is image_button:
    padding (0,0)

screen zn_gallery_replay(source):
    default screenSize = (config.screen_width, config.screen_height)

    zorder 10
    frame:
        style 'zng_replay_image'
        style_prefix 'zng_replay_image'

        imagebutton:
            align (0.5,0.5)
            idle Transform(source, xysize = screenSize)
            action Hide(None, Dissolve(0.2))
