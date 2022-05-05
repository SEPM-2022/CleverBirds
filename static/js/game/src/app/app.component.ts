import {
  AfterViewInit,
  ChangeDetectionStrategy,
  Component,
  HostListener,
  Inject,
} from '@angular/core';
import { DOCUMENT } from '@angular/common';
import { NavigationEnd, Router } from '@angular/router';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class AppComponent implements AfterViewInit {
  title = 'game';

  bird = new Image();
  bg = new Image();
  fg = new Image();
  p1 = new Image();
  p2 = new Image();
  canvas: any;
  context: any;
  constant: any;
  gap = 120;
  gravity = 0.5;
  score = 0;

  birdX = 10;
  birdY = 150;
  pipe: any[] = [];

  constructor(@Inject(DOCUMENT) document: Document, private router: Router) {}

  @HostListener('mousedown', ['$event'])
  @HostListener('document:keydown', ['$event'])
  onMouseDown(e: any) {
    this.moveUp();
  }

  moveUp() {
    this.birdY -= 30;
  }

  draw(): void {
    this.context.drawImage(this.bg, 0, 0);

    this.pipe.forEach(pipe => {
      this.constant = this.p1.height + this.gap;
      this.context.drawImage(this.p1, pipe.x, pipe.y);
      this.context.drawImage(this.p2, pipe.x, pipe.y + this.constant);

      pipe.x--;

      if (pipe.x == 10) {
        this.pipe.push({
          x: this.canvas.width,
          y: Math.floor(Math.random() * this.p1.height) - this.p1.height
        });
      }

      if (this.birdX + this.bird.width >= pipe.x && this.birdX <= pipe.x + this.p1.width && (this.birdY <= pipe.y + this.p1.height || this.birdY + this.bird.height >= pipe.y + this.constant) || this.birdY + this.bird.height >= this.canvas.height - this.fg.height) {
        window.location.href = window.location.search;
      }

      if (pipe.x == 5) {
        this.score++;
      }
    });

    this.context.drawImage(this.fg, 0, this.canvas.height - this.fg.height);
    this.context.drawImage(this.bird, this.birdX, this.birdY);
    this.birdY += this.gravity;

    this.context.fillStyle = 'steelblue';
    this.context.font = '40px Verdana';

    this.context.fillText('Score : ' + this.score, 10, this.canvas.height - 20)

    requestAnimationFrame(this.draw.bind(this));
  }

  ngAfterViewInit(): void {
    this.router.events.subscribe(event => {
      if (event instanceof NavigationEnd) {
        const params = new URLSearchParams(window.location.search)
        const bird = params.get('bird');
        this.canvas = document.getElementById('canvas');
        this.context = this.canvas.getContext('2d');

        this.pipe[0] = { x: this.canvas.width, y: 0 };

        this.bird.src = bird ? `/assets/img/${bird}.png` : '/assets/img/bird.png';
        this.bg.src = '/assets/img/bg.png';
        this.fg.src = '/assets/img/fg.png';
        this.p1.src = '/assets/img/pipeNorth.png';
        this.p2.src = '/assets/img/pipeSouth.png';

        this.draw();
      }
    });
  }
}
