style zng_replay_image is frame:
    background Solid('#bb5858')
    padding (0, 0)
    xysize (1920, 1080)

# style zng_replay_image_image_button is image_button:
#     xysize (1920, 1080)

screen zn_gallery_replay(source):
    frame:
        style 'zng_replay_image'
        style_prefix 'zng_replay_image'

        # image source
        imagebutton:
            # maximum (1620, 800)
            align (0.5,0.5)
            # idle source
            idle source
            # hover Transform(source, xysize=(1920-48, 1080-48))
            padding (0,0)
            action Hide(None, Dissolve(0.2))
