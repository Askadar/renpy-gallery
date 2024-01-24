# HOPE on deez nuts
# Gallery + filters on char + filters on tags + compile of lists from constructors + (support mobile?)
# Gallery - screen + preview buttons
# Image? - screen + fullsize image
# Replay - scene call + return

# Filters - logic to store compiled lists\dicts and use them for sorting

define zngImages = []
define zngTags = {}
define zngCharacters = {}
default persistent.zng_unlocked = False

init python:
    class ZNGalleryImage:
        def __init__(
                self,
                fullsize = None,
                label = None,
                thumbnail = None,
                seenImage = None,
                seenLabel = None,
                tags = None,
                chars = None,
                title = "",
            ):

            if (fullsize is None and label is None) or (fullsize is not None and label is not None):
                raise ValueError("[ZNGalleryImage] You have to pass either `fullsize` image or `label` name. Either is used to open gallery replay. You can't pass both at the same time.")
            if (seenImage is None and seenLabel is None) or (seenImage is not None and seenLabel is not None):
                raise ValueError("[ZNGalleryImage] You have to pass either `seenImage` image or `seenLabel` name. Either is used to enable gallery entry for replay. You can't pass both at the same time.")
            if (tags is None):
                raise ValueError("[ZNGalleryImage] You have to pass list of `tags` that correspond to this gallery item.")
            if (chars is None):
                raise ValueError("[ZNGalleryImage] You have to pass list of `chars` that correspond to this gallery item.")

            self.fullsize = fullsize
            self.label = label
            self.thumbnail = thumbnail
            self.action = ShowTransient('zn_gallery_replay', Dissolve(0.2), fullsize) if fullsize else [Hide("zn_gallery"), Call(label)]
            self.seenImage = seenImage
            self.seenLabel = seenLabel

            self.tags = tags
            self.chars = chars
            self.title = title

        def isImageUnlocked(self):
            return self.seenImage is not None and renpy.seen_image(self.seenImage)

        def isSceneUnlocked(self):
            return self.seenLabel is not None and renpy.seen_label(self.seenLabel)
