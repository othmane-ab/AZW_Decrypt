from xdo import Xdo
import pyautogui
import time

xdo = Xdo()


win_id = xdo.search_windows(winname=b".*Kindle.*", only_visible=True)
if not win_id or len(win_id)>1:
    win_id = xdo.select_window_with_click()
else:
    win_id = win_id[0]

#define next page position
window_size = xdo.get_window_size(win_id)
next_y = 500
next_x = 1523#188
center_x,center_y = 500,500
nbr_pages = 1000

def next_page():
    xdo.activate_window(win_id)
    xdo.move_mouse(next_x, next_y)
    xdo.click_window(win_id, 1)

def first_page():
    xdo.activate_window(win_id)
    xdo.move_mouse(center_x, center_y)
    xdo.click_window(win_id, 1)
i=0
page_prev = None#pyautogui.screenshot(region=(259,138,1207,739))
nbr_retries = 10
while i<nbr_pages and nbr_retries>0:
    try:
        if i==0:
            first_page()
        else:
            next_page()
        page_i = pyautogui.screenshot(region=(259,138,1207,739))
        is_advance = False
        if page_prev is None:
            is_advance = True
        else:
            if list(page_i.getdata())!=list(page_prev.getdata()):
                is_advance = True
        if is_advance:
            page_prev = page_i
            page_i.save(f"Book/book_{i+1}.png")
            i+=1
            print("Done Page", i)
            nbr_retries = 10
        else:
            nbr_retries -= 1
            print("failed 1, tries left", nbr_retries)
    except:
        nbr_retries -= 1
        print("failed 2, tries left", nbr_retries)

    # time.sleep(0.5)
