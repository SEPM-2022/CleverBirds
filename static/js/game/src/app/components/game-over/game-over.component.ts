import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'app-game-over',
  templateUrl: './game-over.component.html'
})
export class GameOverComponent implements OnInit {
  @Input() score: number = 0;

  ngOnInit(): void {
    window.parent.postMessage({score: this.score}, '*');
  }
}
