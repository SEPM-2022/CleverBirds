import { AfterViewChecked, Component, ElementRef, OnInit } from '@angular/core';

@Component({
  selector: 'app-bird',
  templateUrl: './bird.component.html',
  styleUrls: ['./bird.component.scss']
})
export class BirdComponent implements OnInit, AfterViewChecked {
  birdProps: any;

  constructor(private el: ElementRef) {
  }
  ngOnInit(): void {

  }

  ngAfterViewChecked(): void {
    this.birdProps = this.el.nativeElement.getBoundingClientRect();
    console.log('birdProps', this.birdProps);
  }
}
