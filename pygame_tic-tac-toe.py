import pygame
import random
import sys

pygame.init()

# ─── Constants ────────────────────────────────────────────────
WIDTH, HEIGHT = 600, 720
BOARD_TOP = 140
CELL_SIZE = 160
BOARD_LEFT = (WIDTH - CELL_SIZE * 3) // 2
LINE_WIDTH = 5
FPS = 60

# Colors
BG_COLOR      = (15, 15, 25)
GRID_COLOR    = (50, 55, 80)
X_COLOR       = (220, 80, 80)
O_COLOR       = (80, 210, 140)
SCORE_COLOR   = (200, 200, 230)
TITLE_COLOR   = (255, 220, 80)
BTN_COLOR     = (35, 38, 60)
BTN_HOVER     = (55, 60, 95)
BTN_TEXT      = (180, 185, 220)
WIN_LINE_CLR  = (255, 220, 80)
TIE_COLOR     = (150, 150, 200)
SHADOW_COLOR  = (0, 0, 0, 120)

# Fonts
font_title  = pygame.font.SysFont("Segoe UI", 44, bold=True)
font_score  = pygame.font.SysFont("Segoe UI", 24, bold=True)
font_btn    = pygame.font.SysFont("Segoe UI", 20, bold=True)
font_status = pygame.font.SysFont("Segoe UI", 28, bold=True)
font_cell   = pygame.font.SysFont("Segoe UI", 72, bold=True)


# ─── Game State ───────────────────────────────────────────────
class TicTacToe:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Tic-Tac-Toe")
        self.clock = pygame.time.Clock()
        self.reset_all()

    def reset_all(self):
        self.score_x = 0
        self.score_o = 0
        self.count_games = 0
        self.mode = None
        self.start_new_game()

    def start_new_game(self):
        self.board = [''] * 9
        self.used = set()
        if self.count_games % 2 == 0:
            self.current = 'X'
        else:
            self.current = 'O'
        self.winner = None
        self.win_line = None
        self.tie = False
        self.game_over = False
        self.computer_delay = 0

    def draw_bg(self):
        self.screen.fill(BG_COLOR)
        for x in range(0, WIDTH, 40):
            pygame.draw.line(self.screen, (25, 28, 42), (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, 40):
            pygame.draw.line(self.screen, (25, 28, 42), (0, y), (WIDTH, y))

    def draw_title(self):
        title = font_title.render("TIC-TAC-TOE", True, TITLE_COLOR)
        shadow = font_title.render("TIC-TAC-TOE", True, (60, 50, 10))
        self.screen.blit(shadow, (WIDTH//2 - title.get_width()//2 + 2, 22))
        self.screen.blit(title,  (WIDTH//2 - title.get_width()//2, 20))

    def draw_score(self):
        mid = WIDTH // 2
        sy = 78

        ix, iy = mid - 120, sy + 14
        pygame.draw.line(self.screen, X_COLOR, (ix-10, iy-10), (ix+10, iy+10), 3)
        pygame.draw.line(self.screen, X_COLOR, (ix+10, iy-10), (ix-10, iy+10), 3)
        tx = font_score.render(str(self.score_x), True, X_COLOR)
        self.screen.blit(tx, (ix + 16, sy))

        tdash = font_score.render("-", True, GRID_COLOR)
        self.screen.blit(tdash, (mid - tdash.get_width()//2, sy))

        ox, oy = mid + 95, sy + 14
        pygame.draw.circle(self.screen, O_COLOR, (ox, oy), 10, 3)
        to_surf = font_score.render(str(self.score_o), True, O_COLOR)
        self.screen.blit(to_surf, (ox + 16, sy))

    def draw_grid(self):
        for row in range(1, 3):
            y = BOARD_TOP + row * CELL_SIZE
            pygame.draw.line(self.screen, GRID_COLOR,
                             (BOARD_LEFT + 8, y), (BOARD_LEFT + CELL_SIZE*3 - 8, y), LINE_WIDTH)
        for col in range(1, 3):
            x = BOARD_LEFT + col * CELL_SIZE
            pygame.draw.line(self.screen, GRID_COLOR,
                             (x, BOARD_TOP + 8), (x, BOARD_TOP + CELL_SIZE*3 - 8), LINE_WIDTH)

    def draw_cells(self):
        for i, val in enumerate(self.board):
            row, col = divmod(i, 3)
            cx = BOARD_LEFT + col * CELL_SIZE + CELL_SIZE // 2
            cy = BOARD_TOP  + row * CELL_SIZE + CELL_SIZE // 2
            if val == 'X':
                self._draw_x(cx, cy)
            elif val == 'O':
                self._draw_o(cx, cy)

    def _draw_x(self, cx, cy):
        r, w = 42, 8
        pygame.draw.line(self.screen, (80, 20, 20), (cx-r+3, cy-r+3), (cx+r+3, cy+r+3), w+2)
        pygame.draw.line(self.screen, (80, 20, 20), (cx+r+3, cy-r+3), (cx-r+3, cy+r+3), w+2)
        pygame.draw.line(self.screen, X_COLOR, (cx-r, cy-r), (cx+r, cy+r), w)
        pygame.draw.line(self.screen, X_COLOR, (cx+r, cy-r), (cx-r, cy+r), w)

    def _draw_o(self, cx, cy):
        r, w = 44, 8
        pygame.draw.circle(self.screen, (20, 80, 50), (cx+3, cy+3), r, w+2)
        pygame.draw.circle(self.screen, O_COLOR, (cx, cy), r, w)

    def draw_win_line(self):
        if self.win_line is None:
            return
        i1, i2 = self.win_line[0], self.win_line[-1]
        r1, c1 = divmod(i1, 3)
        r2, c2 = divmod(i2, 3)
        x1 = BOARD_LEFT + c1 * CELL_SIZE + CELL_SIZE // 2
        y1 = BOARD_TOP  + r1 * CELL_SIZE + CELL_SIZE // 2
        x2 = BOARD_LEFT + c2 * CELL_SIZE + CELL_SIZE // 2
        y2 = BOARD_TOP  + r2 * CELL_SIZE + CELL_SIZE // 2
        pygame.draw.line(self.screen, WIN_LINE_CLR, (x1, y1), (x2, y2), 8)

    def draw_status(self):
        y = BOARD_TOP + CELL_SIZE * 3 + 16
        cx = WIDTH // 2

        def draw_icon(x, y, player, size=12, lw=4):
            if player == 'X':
                pygame.draw.line(self.screen, X_COLOR, (x-size, y-size), (x+size, y+size), lw)
                pygame.draw.line(self.screen, X_COLOR, (x+size, y-size), (x-size, y+size), lw)
            else:
                pygame.draw.circle(self.screen, O_COLOR, (x, y), size, lw)

        if self.game_over:
            if self.tie:
                surf = font_status.render("Its a Tie!", True, TIE_COLOR)
                self.screen.blit(surf, (cx - surf.get_width()//2, y))
            else:
                color = X_COLOR if self.winner == 'X' else O_COLOR
                txt = font_status.render("Wins!", True, color)
                total_w = 28 + txt.get_width()
                start_x = cx - total_w // 2
                icon_cy = y + txt.get_height() // 2
                draw_icon(start_x + 12, icon_cy, self.winner)
                self.screen.blit(txt, (start_x + 28, y))
        else:
            if self.mode is None:
                return
            color = X_COLOR if self.current == 'X' else O_COLOR
            lbl = "Your turn" if (self.mode == 1 or self.current == 'X') else "Computer..."
            txt = font_status.render(lbl, True, color)
            total_w = 28 + txt.get_width()
            start_x = cx - total_w // 2
            icon_cy = y + txt.get_height() // 2
            draw_icon(start_x + 12, icon_cy, self.current, size=11)
            self.screen.blit(txt, (start_x + 28, y))

    def draw_buttons(self):
        if self.mode is None:
            buttons = [("2 Players", self._btn(0)), ("vs Computer", self._btn(1))]
        else:
            if self.game_over:
                buttons = [("Play Again", self._btn(0)), ("Main Menu", self._btn(1)), ("Reset Scores", self._btn(2))]
            else:
                buttons = [("Main Menu", self._btn(0)), ("Reset Scores", self._btn(1))]

        mx, my = pygame.mouse.get_pos()
        self._buttons_cache = []
        for label, rect in buttons:
            hovered = rect.collidepoint(mx, my)
            color = BTN_HOVER if hovered else BTN_COLOR
            pygame.draw.rect(self.screen, color, rect, border_radius=10)
            pygame.draw.rect(self.screen, GRID_COLOR, rect, 2, border_radius=10)
            txt = font_btn.render(label, True, BTN_TEXT)
            self.screen.blit(txt, (rect.centerx - txt.get_width()//2, rect.centery - txt.get_height()//2))
            self._buttons_cache.append((label, rect))

    def _btn(self, index):
        btn_w, btn_h = 160, 42
        gap = 18
        n = 3 if (self.game_over and self.mode is not None) else 2
        all_w = n * btn_w + (n-1) * gap
        start_x = (WIDTH - all_w) // 2
        y = BOARD_TOP + CELL_SIZE*3 + 60
        x = start_x + index * (btn_w + gap)
        return pygame.Rect(x, y, btn_w, btn_h)

    def check_winner(self):
        wins = [(0,1,2),(3,4,5),(6,7,8),
                (0,3,6),(1,4,7),(2,5,8),
                (0,4,8),(2,4,6)]
        for a, b, c in wins:
            if self.board[a] == self.board[b] == self.board[c] and self.board[a]:
                return self.board[a], [a, b, c]
        return None, None

    def is_board_full(self):
        return all(v != '' for v in self.board)

    def make_move(self, idx):
        if idx in self.used or self.board[idx] or self.game_over:
            return False
        self.board[idx] = self.current
        self.used.add(idx)
        winner, line = self.check_winner()
        if winner:
            self.winner = winner
            self.win_line = line
            self.game_over = True
            if winner == 'X':
                self.score_x += 1
            else:
                self.score_o += 1
        elif self.is_board_full():
            self.tie = True
            self.game_over = True
        else:
            self.current = 'O' if self.current == 'X' else 'X'
        return True

    def computer_move(self):
        empty = [i for i in range(9) if not self.board[i]]
        if empty:
            self.make_move(random.choice(empty))

    def cell_at(self, pos):
        mx, my = pos
        col = (mx - BOARD_LEFT) // CELL_SIZE
        row = (my - BOARD_TOP)  // CELL_SIZE
        if 0 <= col < 3 and 0 <= row < 3:
            return row * 3 + col
        return None

    def handle_button_click(self, pos):
        if not hasattr(self, '_buttons_cache'):
            return
        for label, rect in self._buttons_cache:
            if rect.collidepoint(pos):
                if label == "2 Players":
                    self.mode = 1
                    self.count_games = 0
                    self.start_new_game()
                elif label == "vs Computer":
                    self.mode = 2
                    self.count_games = 0
                    self.start_new_game()
                elif label == "Play Again":
                    self.count_games += 1
                    self.start_new_game()
                elif label == "Main Menu":
                    self.mode = None
                    self.start_new_game()
                elif label == "Reset Scores":
                    self.score_x = 0
                    self.score_o = 0
                    self.count_games = 0
                    self.start_new_game()

    def run(self):
        while True:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    pos = event.pos
                    if self.mode is not None and not self.game_over:
                        if self.mode == 1 or (self.mode == 2 and self.current == 'X'):
                            idx = self.cell_at(pos)
                            if idx is not None:
                                self.make_move(idx)
                                if self.mode == 2 and not self.game_over:
                                    self.computer_delay = 40
                    self.handle_button_click(pos)

            if (self.mode == 2 and not self.game_over
                    and self.current == 'O' and self.computer_delay > 0):
                self.computer_delay -= 1
                if self.computer_delay == 0:
                    self.computer_move()

            self.draw_bg()
            self.draw_title()
            self.draw_score()
            if self.mode is not None:
                self.draw_grid()
                self.draw_cells()
                if self.game_over:
                    self.draw_win_line()
            self.draw_status()
            self.draw_buttons()
            pygame.display.flip()


if __name__ == '__main__':
    game = TicTacToe()
    game.run()