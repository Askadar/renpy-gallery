# HOPE on deez nuts
# Gallery + filters on char + filters on tags + compile of lists from constructors + (support mobile?)
# Gallery - screen + preview buttons
# Image? - screen + fullsize image
# Replay - scene call + return

# Filters - logic to store compiled lists\dicts and use them for sorting

define zngImages = []
default persistent.zng_unlocked = False

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
            self.action = ShowTransient('zn_gallery_replay', Dissolve(0.2), fullsize) if fullsize else Call(label)
            self.seenImage = seenImage
            self.seenLabel = seenLabel
