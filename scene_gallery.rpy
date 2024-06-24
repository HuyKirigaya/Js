default persistent.name = ""

default scopeDict = {}



init python:

    class SceneGallery:

        def __init__(

            self, title: str, image: str, label: str, scope: Optional[dict[str, Any]] = None

        ):

            self.title = title

            self.image = image

            self.label = label



            if scope is None:

                self.scope = {}

            else:

                self.scope = scope



            scene_gallery_items.append(self)





    def update_scope(new_scope: dict[str, Any]):

        rv: dict[str, Any] = scopeDict.copy()

        rv.update(new_scope)

        return rv



    scene_gallery_items: list[SceneGallery] = []



    # v1

    if renpy.loadable("v1/scene1.rpy"):

        SceneGallery("Chạy về nơi phía anh", "images/v1/scene 21a/v1chlcgTPP.webp", "v1s21a") # 21a, Chloe, xx

        SceneGallery("Suy nghĩ trong anh", "images/v1/scene 25a/v1s25a_17.webp", "v1s25a") # 25a, Amber, xx

        SceneGallery("Bông hoa đẹp nhất", "images/v1/scene 36/v1jenmo2Start.webp", "v1s36_sg") # 36, Jenny, xx

        SceneGallery("Sao em nỡ", "images/v1/scene 46a/v1s46a_12.webp", "v1s46a_sga") # 46a, Lauren good (scope is Lauren GIRLFRIEND)

        SceneGallery("Lý ngựa ô", "images/v1/scene 46a/v1s46a_27c.webp", "v1s46a_sgb") # 46a, Lauren bad

        SceneGallery("Em ơi đừng sầu", "images/v1/scene 53a/v1s53a_16.webp", "v1s53_sg") # 53a, Samantha, xx



    # v2

    if renpy.loadable("v2/scene1.rpy"):

        SceneGallery("Giận mà thương", "images/v2/scene 15/v2s15_7f.webp", "v2s15sg") # 15, Ms. Rose

        SceneGallery("Điều anh biết", "images/v2/scene 18a/v2s18aamber_9e.webp", "v2s18a_ambersg") # 18a, Amber

        SceneGallery("Thuận theo ý trời", "images/v2/scene 18c/v2s18c_imau_14.webp", "v2s18c_aubreysg") # 18c, Aubrey

        SceneGallery("Không quan tâm", "images/v2/scene 18c/v2autkiss.webp", "v2s18c_autumnsg") # 18c, Autumn

        SceneGallery("Phía sau một cô gái", "images/v2/scene 18c/v2s18c_chpe_11.webp", "v2s18c_penelopesg") # 18c, Penelope

        SceneGallery("Gác lại âu lo", "images/v2/scene 18a/v2s18ariley_14.webp", "v2s18a_rileysg") # 18a, Riley

        SceneGallery("Khúc hát mừng sinh nhật", "images/v2/scene 18e/v2s18eend_6.webp", "v2s18e_sg") # 18e, Lauren

        SceneGallery("Tận cùng nỗi nhớ", "images/v2/scene 29/v2s29_emily_lingerie.webp", "v2s29_emilysg") # 18e, Lauren

        SceneGallery("Nợ ai đó lời xin lỗi", "images/v2/scene 33/v2s33_46b.webp", "v2s35_naomisg") # 33, Naomi

        SceneGallery("Cố giang tình", "images/v2/scene 48a/v2noror2Start.webp", "v2s48a_norasg") # 48, Nora



    # v3

    if renpy.loadable("v3/scene1.rpy"):

        SceneGallery("Ký sự đấm mồm Tom", "images/v3/Scene 1/fight/tom-stances/v3-tom-stance-def.webp", "v3s1") # 1, Tom

        SceneGallery("Cầu vồng sau mưa", "images/v3/scene 3a/v3s3a_1a.webp", "v3s3a") # 3a, Riley

        SceneGallery("Em yêu vội thế", "images/v3/scene 10/v3s10_2g.webp", "v3s10_sg") # 10, Lauren

        SceneGallery("Một vòng trái đất", "images/v3/scene 25/v3s25_11h.webp", "v3s25_sg") # 25, Emily

        SceneGallery("Bố Là Tất Cả", "images/v3/Scene 48a/v3chlfgStart.webp", "v3s48a") # 48, Chloe

        SceneGallery("Cả một trời thương nhớ", "images/v3/Scene 63a/v3norfgStart.webp", "v3s63_sg") # 63a, Nora

        SceneGallery("Bông hoa đẹp nhất", "images/v3/Scene 63c/v3linbjStart.webp", "v3s63c_sg") # 63c, Lindsey

        SceneGallery("Nhỏ ơi", "images/v3/Scene 71a/v3penst2Start.webp", "v3s71_sg") # 71a, Penelope



screen scene_gallery():

    tag menu

    modal True

    style_prefix "scene_gallery"



    default image_path = "main_menu/scene_gallery/images/"



    add image_path + "background.webp"



    imagebutton:

        idle image_path + "return_idle.webp"

        hover image_path + "return_hover.webp"

        action ShowMenu("main_menu")

        pos (120, 80)



    # Gallery unlock

    if achievement.steam and achievement.steam.dlc_installed(1929620):

        frame:

            xalign 1.0

            xoffset -50

            ypos 50



            if persistent.gallery_lock is None:

                textbutton "Mở khóa cảnh nóng \nchưa mở được":

                    action SetField(persistent, "gallery_lock", False)

                    text_size 36

            else:

                textbutton "Khóa cảnh nóng \nchưa mở được":

                    action SetField(persistent, "gallery_lock", None)

                    text_size 36



    fixed:

        pos (114, 178)

        ypos 178

        xysize (1688, 830)



        vpgrid id "vpg":

            cols 4

            spacing 20

            xalign 0.5

            top_margin 50

            bottom_margin 80

            mousewheel True

            allow_underfull True

            

            for gallery_item in scene_gallery_items:

                frame:

                    xysize (374, 300)



                    button:

                        background Transform(gallery_item.image, size=(362, 230), pos=(6, 16))

                        insensitive_background Transform(gallery_item.image, blur=50, size=(362, 230), pos=(6, 16))

                        idle_foreground image_path + "button_idle.webp"

                        hover_foreground image_path + "button_hover.webp"

                        insensitive_foreground image_path + "button_idle.webp"

                        action Replay(gallery_item.label, scope=update_scope(gallery_item.scope), locked=False)

                    frame:

                        xysize (250, 49)

                        xalign 0.5

                        ypos 224



                        text gallery_item.title.upper() align (0.5, 0.5)



            null



    add image_path + "shadow.webp" xalign 0.5 ypos 893



    add Transform("scene_gallery_bar_base", size=(27, 734)) pos (1743, 226)

    vbar:

        pos (1748, 231)

        xysize (17, 724)

        base_bar "#0000"

        thumb "gui/bar/bar_thumb.webp"

        value YScrollValue("vpg")





style scene_gallery_text is bebas_neue_30:

    size 22





label scene_gallery_name_change:

    scene black

    if not persistent.name.strip():

        $ persistent.name = renpy.input(_("Làm cái tên đi bro"), default=_("Alex")).strip() or _("Alex")



    $ scopeDict = {"name": persistent.name}



    return
