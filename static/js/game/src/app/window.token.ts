import { InjectionToken } from '@angular/core';

export const WINDOW_TOKEN = {
  LOCATION: new InjectionToken<Location>('Window location object')
};
