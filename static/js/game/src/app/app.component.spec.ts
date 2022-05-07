import { ComponentFixture, TestBed } from '@angular/core/testing';
import { RouterTestingModule } from '@angular/router/testing';
import { AppComponent } from './app.component';
import { NavigationEnd, Router } from '@angular/router';
import { WINDOW_TOKEN } from './window.token';
import { Subject } from 'rxjs';
import { CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';

describe('AppComponent', () => {
  const mockLocation = {
    href: ''
  };
  let component: AppComponent;
  let fixture: ComponentFixture<AppComponent>;
  let router: Router;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [
        RouterTestingModule
      ],
      declarations: [
        AppComponent
      ],
      providers: [
        { provide: WINDOW_TOKEN.LOCATION, useValue: mockLocation },
      ],
      schemas: [CUSTOM_ELEMENTS_SCHEMA]
    }).compileComponents();

    fixture = TestBed.createComponent(AppComponent);
    component = fixture.componentInstance;
    router = TestBed.inject(Router);

    fixture.detectChanges();
  });

  it(`should have as title 'game'`, () => {
    expect(component.title).toEqual('game');
  });

  it('should update y-axis of bird onMouseDown', () => {
    component.birdY = 40;

    component.onMouseDown(new MouseEvent('mousedown'));

    expect(component.birdY).toBe(10);
  });

  it('should set assets and call draw method once app has loaded', () => {
    const bird = 'alfredo';
    const event1 = new NavigationEnd(1, `/?bird=${bird}`, '/');
    component.draw = jest.fn();

    component.ngAfterViewInit();
    (router.events as unknown as Subject<NavigationEnd>).next(event1);

    expect(component.draw).toHaveBeenCalled();
    expect(component.bird.src).toBe(`http://localhost/assets/img/${bird}.png`);
    expect(component.bg.src).toBe('http://localhost/assets/img/bg2_small.png');
    expect(component.fg.src).toBe('http://localhost/assets/img/fg_edited.png');
    expect(component.pipeNorth.src).toBe('http://localhost/assets/img/pipeNorth_edited.png');
    expect(component.pipeSouth.src).toBe('http://localhost/assets/img/pipeSouth_edited.png');
  });

  it('should set bird to "birdy" if bird param wasnt set', () => {
    const bird = 'birdy';
    const event1 = new NavigationEnd(1, `/`, '/');
    component.draw = jest.fn();

    component.ngAfterViewInit();
    (router.events as unknown as Subject<NavigationEnd>).next(event1);

    expect(component.draw).toHaveBeenCalled();
    expect(component.bird.src).toBe(`http://localhost/assets/img/${bird}.png`);
  });

  it('should set defaults correctly on first draw call', () => {
    const birdY = 150;
    component.birdY = birdY;
    component.canvas = document.getElementById('canvas') as HTMLCanvasElement;
    component.context = component.canvas.getContext('2d') as CanvasRenderingContext2D;
    component.context.drawImage = jest.fn();

    component.draw();

    expect(component.context.drawImage).toHaveBeenCalledWith(component.bg, 0, 0);
    expect(component.context.drawImage).toHaveBeenCalledWith(component.fg, 0, component.canvas.height - component.fg.height);
    expect(component.context.drawImage).toHaveBeenCalledWith(component.fg, 288, component.canvas.height - component.fg.height);
    expect(component.context.drawImage).toHaveBeenCalledWith(component.fg, 576, component.canvas.height - component.fg.height);
    expect(component.context.drawImage).toHaveBeenCalledWith(component.bird, component.birdX, birdY);
    expect(component.birdY).toBe(birdY + component.gravity);
  });

  it('should show game over when pipe was hit', () => {
    component.canvas = document.getElementById('canvas') as HTMLCanvasElement;
    component.context = component.canvas.getContext('2d') as CanvasRenderingContext2D;
    component.pipe[0] = { x: 20, y: 0 };
    component.birdX = 10;
    component.bird.width = 10;

    component.draw();

    expect(component.state).toBe('gameover');
  });

  it('should show game over when out of bounds', () => {
    component.canvas = document.getElementById('canvas') as HTMLCanvasElement;
    component.context = component.canvas.getContext('2d') as CanvasRenderingContext2D;
    component.pipe[0] = { x: 21, y: 0 };
    component.birdX = 10;
    component.birdY = 100;
    component.bird.width = 10;
    component.bird.height = 10;
    component.canvas.height = 120;
    component.fg.height = 10;

    component.draw();

    expect(component.state).toBe('gameover');
  });
});
