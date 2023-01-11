import { Component, OnInit } from '@angular/core';
import { Objects } from 'src/app/models/objects.model';
import { ObjectsService } from 'src/app/services/objects.service';

@Component({
  selector: 'app-object-tab',
  templateUrl: './object-tab.component.html',
  styleUrls: ['./object-tab.component.css']
})
export class ObjectTabComponent implements OnInit {
  objects?: Objects[];
  currentObject: Objects = {};
  currentIndex = -1;
  title = '';

  constructor(private objectService: ObjectsService) { }

  ngOnInit(): void {
    this.retrieveObjects();
  }

  retrieveObjects(): void {
    this.objectService.getAll()
      .subscribe({
        next: (data) => {
          this.objects = data;
          console.log(data);
        },
        error: (e) => console.error(e)
      });
  }

  refreshList(): void {
    this.retrieveObjects();
    this.currentObject = {};
    this.currentIndex = -1;
  }

}
