from typing import Any, Dict

import pygame

from configs import config


class PopupBuilder:
    def init_popup(
        screen: pygame.Surface, mode: str = "save_success"
    ) -> Dict[str, Any]:
        popup_settings: Dict[str, Dict[str, Any]] = config.popup_settings

        font = pygame.font.Font(None, popup_settings[mode]["font_size"])
        text_surf = font.render(
            popup_settings[mode]["message"], True, popup_settings[mode]["text_color"]
        )
        text_rect = text_surf.get_rect(center=popup_settings[mode]["position"])

        bg_surf = pygame.Surface((text_rect.width + 20, text_rect.height + 20))
        bg_surf.set_alpha(popup_settings[mode]["alpha"])
        bg_surf.fill(popup_settings[mode]["bg_color"])
        bg_rect = bg_surf.get_rect(center=popup_settings[mode]["position"])

        start_time = pygame.time.get_ticks()

        return {
            "text_surf": text_surf,
            "text_rect": text_rect,
            "bg_surf": bg_surf,
            "bg_rect": bg_rect,
            "start_time": start_time,
            "duration": popup_settings[mode]["duration"] * 1000,
        }

    def draw_popup(screen: pygame.Surface, popup_info: Dict[str, Any]) -> bool:
        current_time: pygame.time = pygame.time.get_ticks()

        if current_time - popup_info["start_time"] < popup_info["duration"]:
            screen.blit(popup_info["bg_surf"], popup_info["bg_rect"])
            screen.blit(popup_info["text_surf"], popup_info["text_rect"])
            return True
        return False
