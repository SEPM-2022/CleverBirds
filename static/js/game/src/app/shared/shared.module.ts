import { CommonModule } from '@angular/common';
import { NgModule } from '@angular/core';
import { BirdComponent } from 'src/app/shared/components/bird/bird.component';

@NgModule({
  imports: [CommonModule],
  declarations: [BirdComponent],
  exports: [CommonModule, BirdComponent]
})
export class SharedModule {}
