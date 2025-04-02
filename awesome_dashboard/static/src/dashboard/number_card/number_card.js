import { Component } from "@odoo/owl";
 
 export class NumberCard extends Component {
     static template = "gabriela-awesome_dashboard.NumberCard";
     static props = {
         title: {
             type: String,
         },
         value: {
             type: Number,
         }
     }
 }