import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 600, 680
CELL_SIZE = 150
BOARD_LEFT = (WIDTH - CELL_SIZE * 3) // 2
BOARD_TOP  = 120
LINE_WIDTH = 5
FPS = 60

BG_COLOR     = (15, 15, 25)
GRID_COLOR   = (50, 55, 80)
X_COLOR      = (220, 80, 80)
O_COLOR      = (80, 210, 140)
TITLE_COLOR  = (255, 220, 80)
BTN_COLOR    = (35, 38, 60)
BTN_HOVER    = (55, 60, 95)
BTN_TEXT     = (180, 185, 220)
WIN_LINE_CLR = (255, 220, 80)
TIE_COLOR    = (150, 150, 200)
HIGHLIGHT    = (255, 220, 80)

font_title  = pygame.font.SysFont("Segoe UI", 40, bold=True)
font_score  = pygame.font.SysFont("Segoe UI", 22, bold=True)
font_btn    = pygame.font.SysFont("Segoe UI", 18, bold=True)
font_status = pygame.font.SysFont("Segoe UI", 24, bold=True)
font_small  = pygame.font.SysFont("Segoe UI", 16, bold=True)


class TicTacToe:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Tic-Tac-Toe")
        self.clock = pygame.time.Clock()
        self.score_x = 0
        self.score_o = 0
        self.mode = None
        self.first_player = 'X'
        self.start_new_game()

    def start_new_game(self):
        self.board = [''] * 9
        self.used  = set()
        self.current   = self.first_player
        self.winner    = None
        self.win_line  = None
        self.tie       = False
        self.game_over = False
        # If vs computer and O starts — computer moves first after short delay
        self.computer_delay = 40 if (self.mode == 2 and self.first_player == 'O') else 0

    # ── drawing helpers ───────────────────────────────────────
    def draw_icon(self, x, y, player, size=12, lw=4):
        if player == 'X':
            pygame.draw.line(self.screen, X_COLOR, (x-size, y-size), (x+size, y+size), lw)
            pygame.draw.line(self.screen, X_COLOR, (x+size, y-size), (x-size, y+size), lw)
        else:
            pygame.draw.circle(self.screen, O_COLOR, (x, y), size, lw)

    def draw_bg(self):
        self.screen.fill(BG_COLOR)
        for x in range(0, WIDTH, 40):
            pygame.draw.line(self.screen, (25,28,42), (x,0), (x,HEIGHT))
        for y in range(0, HEIGHT, 40):
            pygame.draw.line(self.screen, (25,28,42), (0,y), (WIDTH,y))

    def draw_title(self):
        t = font_title.render("TIC-TAC-TOE", True, TITLE_COLOR)
        s = font_title.render("TIC-TAC-TOE", True, (60,50,10))
        self.screen.blit(s, (WIDTH//2 - t.get_width()//2 + 2, 12))
        self.screen.blit(t, (WIDTH//2 - t.get_width()//2,     10))

    def draw_score(self):
        mid, sy = WIDTH//2, 62
        # X icon + score
        ix, iy = mid-110, sy+12
        self.draw_icon(ix, iy, 'X', size=9, lw=3)
        tx = font_score.render(str(self.score_x), True, X_COLOR)
        self.screen.blit(tx, (ix+14, sy))
        # dash
        d = font_score.render("-", True, GRID_COLOR)
        self.screen.blit(d, (mid - d.get_width()//2, sy))
        # O icon + score
        ox, oy = mid+85, sy+12
        pygame.draw.circle(self.screen, O_COLOR, (ox,oy), 9, 3)
        to = font_score.render(str(self.score_o), True, O_COLOR)
        self.screen.blit(to, (ox+14, sy))

    def draw_status(self):
        # row between score and board
        y  = BOARD_TOP - 32
        cx = WIDTH // 2
        if self.mode is None:
            # show who starts
            lbl = font_small.render("Starts:", True, HIGHLIGHT)
            total = lbl.get_width() + 24
            sx = cx - total//2
            self.screen.blit(lbl, (sx, y+3))
            self.draw_icon(sx + lbl.get_width() + 16, y + lbl.get_height()//2 + 3,
                           self.first_player, size=9, lw=3)
        elif self.game_over:
            if self.tie:
                surf = font_status.render("Its a Tie!", True, TIE_COLOR)
                self.screen.blit(surf, (cx - surf.get_width()//2, y))
            else:
                color = X_COLOR if self.winner=='X' else O_COLOR
                txt   = font_status.render("Wins!", True, color)
                tw    = 26 + txt.get_width()
                sx    = cx - tw//2
                self.draw_icon(sx+11, y+txt.get_height()//2, self.winner, size=11)
                self.screen.blit(txt, (sx+24, y))
        else:
            color = X_COLOR if self.current=='X' else O_COLOR
            if self.mode == 2 and self.current == 'O':
                lbl = "Computer..."
            else:
                lbl = "Your turn"
            txt = font_status.render(lbl, True, color)
            tw  = 26 + txt.get_width()
            sx  = cx - tw//2
            self.draw_icon(sx+11, y+txt.get_height()//2, self.current, size=11)
            self.screen.blit(txt, (sx+24, y))

    def draw_grid(self):
        for row in range(1, 3):
            y = BOARD_TOP + row*CELL_SIZE
            pygame.draw.line(self.screen, GRID_COLOR,
                             (BOARD_LEFT+6,y), (BOARD_LEFT+CELL_SIZE*3-6,y), LINE_WIDTH)
        for col in range(1, 3):
            x = BOARD_LEFT + col*CELL_SIZE
            pygame.draw.line(self.screen, GRID_COLOR,
                             (x,BOARD_TOP+6), (x,BOARD_TOP+CELL_SIZE*3-6), LINE_WIDTH)

    def draw_cells(self):
        for i, val in enumerate(self.board):
            row, col = divmod(i, 3)
            cx = BOARD_LEFT + col*CELL_SIZE + CELL_SIZE//2
            cy = BOARD_TOP  + row*CELL_SIZE + CELL_SIZE//2
            if val == 'X': self._draw_x(cx, cy)
            elif val == 'O': self._draw_o(cx, cy)

    def _draw_x(self, cx, cy):
        r, w = 38, 8
        pygame.draw.line(self.screen, (80,20,20), (cx-r+3,cy-r+3),(cx+r+3,cy+r+3), w+2)
        pygame.draw.line(self.screen, (80,20,20), (cx+r+3,cy-r+3),(cx-r+3,cy+r+3), w+2)
        pygame.draw.line(self.screen, X_COLOR, (cx-r,cy-r),(cx+r,cy+r), w)
        pygame.draw.line(self.screen, X_COLOR, (cx+r,cy-r),(cx-r,cy+r), w)

    def _draw_o(self, cx, cy):
        r, w = 40, 8
        pygame.draw.circle(self.screen, (20,80,50), (cx+3,cy+3), r, w+2)
        pygame.draw.circle(self.screen, O_COLOR, (cx,cy), r, w)

    def draw_win_line(self):
        if not self.win_line: return
        i1, i2 = self.win_line[0], self.win_line[-1]
        r1,c1 = divmod(i1,3); r2,c2 = divmod(i2,3)
        x1 = BOARD_LEFT + c1*CELL_SIZE + CELL_SIZE//2
        y1 = BOARD_TOP  + r1*CELL_SIZE + CELL_SIZE//2
        x2 = BOARD_LEFT + c2*CELL_SIZE + CELL_SIZE//2
        y2 = BOARD_TOP  + r2*CELL_SIZE + CELL_SIZE//2
        pygame.draw.line(self.screen, WIN_LINE_CLR, (x1,y1),(x2,y2), 8)

    def _make_buttons(self):
        btn_w, btn_h, gap = 148, 38, 10
        base_y = BOARD_TOP + CELL_SIZE*3 + 16

        if self.mode is None:
            all_w = 2*btn_w + gap
            sx = (WIDTH - all_w)//2
            btns = [
                ("2 Players",   pygame.Rect(sx,           base_y, btn_w, btn_h)),
                ("vs Computer", pygame.Rect(sx+btn_w+gap, base_y, btn_w, btn_h)),
            ]
            sw_w = btn_w + 50
            btns.append(("Switch Start",
                          pygame.Rect((WIDTH-sw_w)//2, base_y+btn_h+8, sw_w, btn_h)))
        elif self.game_over:
            labels = ["Play Again","Main Menu","Reset Scores"]
            all_w  = len(labels)*btn_w + (len(labels)-1)*gap
            sx = (WIDTH-all_w)//2
            btns = [(lbl, pygame.Rect(sx+i*(btn_w+gap), base_y, btn_w, btn_h))
                    for i,lbl in enumerate(labels)]
        else:
            labels = ["Main Menu","Reset Scores"]
            all_w  = len(labels)*btn_w + (len(labels)-1)*gap
            sx = (WIDTH-all_w)//2
            btns = [(lbl, pygame.Rect(sx+i*(btn_w+gap), base_y, btn_w, btn_h))
                    for i,lbl in enumerate(labels)]
        return btns

    def draw_buttons(self):
        mx, my = pygame.mouse.get_pos()
        self._buttons_cache = self._make_buttons()
        for label, rect in self._buttons_cache:
            is_sw   = (label == "Switch Start")
            hovered = rect.collidepoint(mx, my)
            bg  = ((60,56,18) if hovered else (42,40,12)) if is_sw else (BTN_HOVER if hovered else BTN_COLOR)
            bdr = HIGHLIGHT if is_sw else GRID_COLOR
            pygame.draw.rect(self.screen, bg,  rect, border_radius=9)
            pygame.draw.rect(self.screen, bdr, rect, 2, border_radius=9)
            if is_sw:
                lbl_s = font_small.render("Starts:", True, HIGHLIGHT)
                total = lbl_s.get_width() + 24
                lx    = rect.centerx - total//2
                ly    = rect.centery - lbl_s.get_height()//2
                self.screen.blit(lbl_s, (lx, ly))
                self.draw_icon(lx+lbl_s.get_width()+16, rect.centery,
                               self.first_player, size=9, lw=3)
            else:
                txt = font_btn.render(label, True, BTN_TEXT)
                self.screen.blit(txt, (rect.centerx-txt.get_width()//2,
                                       rect.centery-txt.get_height()//2))

    # ── logic ─────────────────────────────────────────────────
    def check_winner(self):
        wins = [(0,1,2),(3,4,5),(6,7,8),
                (0,3,6),(1,4,7),(2,5,8),
                (0,4,8),(2,4,6)]
        for a,b,c in wins:
            if self.board[a]==self.board[b]==self.board[c] and self.board[a]:
                return self.board[a],[a,b,c]
        return None,None

    def make_move(self, idx):
        if idx in self.used or self.board[idx] or self.game_over:
            return False
        self.board[idx] = self.current
        self.used.add(idx)
        winner, line = self.check_winner()
        if winner:
            self.winner, self.win_line, self.game_over = winner, line, True
            if winner=='X': self.score_x += 1
            else:           self.score_o += 1
        elif all(self.board):
            self.tie = self.game_over = True
        else:
            self.current = 'O' if self.current=='X' else 'X'
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
            return row*3 + col
        return None

    def handle_click(self, pos):
        if self.mode is not None and not self.game_over:
            if self.mode==1 or (self.mode==2 and self.current=='X'):
                idx = self.cell_at(pos)
                if idx is not None:
                    self.make_move(idx)
                    if self.mode==2 and not self.game_over:
                        self.computer_delay = 40
        if not hasattr(self, '_buttons_cache'): return
        for label, rect in self._buttons_cache:
            if rect.collidepoint(pos):
                if label == "2 Players":
                    self.mode=1; self.start_new_game()
                elif label == "vs Computer":
                    self.mode=2; self.start_new_game()
                elif label == "Switch Start":
                    self.first_player = 'O' if self.first_player=='X' else 'X'
                elif label == "Play Again":
                    self.start_new_game()
                elif label == "Main Menu":
                    self.mode=None; self.start_new_game()
                elif label == "Reset Scores":
                    self.score_x=self.score_o=0; self.start_new_game()

    # ── main loop ─────────────────────────────────────────────
    def run(self):
        while True:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit(); sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button==1:
                    self.handle_click(event.pos)

            # computer turn (also handles first move when O starts)
            if (self.mode==2 and not self.game_over
                    and self.current=='O' and self.computer_delay > 0):
                self.computer_delay -= 1
                if self.computer_delay == 0:
                    self.computer_move()

            self.draw_bg()
            self.draw_title()
            self.draw_score()
            self.draw_status()
            if self.mode is not None:
                self.draw_grid()
                self.draw_cells()
                if self.game_over:
                    self.draw_win_line()
            self.draw_buttons()
            pygame.display.flip()


if __name__ == '__main__':
    TicTacToe().run()