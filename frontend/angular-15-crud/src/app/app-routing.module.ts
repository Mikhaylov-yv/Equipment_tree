import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ObjectTabComponent } from './components/object-tab/object-tab.component';

const routes: Routes = [
  { path: '', redirectTo: 'object_tab', pathMatch: 'full' }, 
  { path: 'object_tab', component : ObjectTabComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
